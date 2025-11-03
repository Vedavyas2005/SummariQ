import streamlit as st
import os
import uuid

import auth
import db
import rag
import llm
import utils

st.set_page_config(page_title="SummariQ", layout="wide")

def sidebar_user_panel():
    st.sidebar.title("SummariQ")
    logged_in = st.session_state.get("logged_in", False)
    user_id = st.session_state.get("user_id") if logged_in else None
    if logged_in:
        st.sidebar.write(f"**Logged in as:** `{st.session_state.username}`")
        if st.sidebar.button("Logout"):
            st.session_state.clear()
            st.rerun()
        st.sidebar.markdown("---")
        st.sidebar.header("Recent Sessions")
        chats = db.get_chats(user_id)
        for chat in chats:
            if st.sidebar.button(f"{chat['timestamp']} - {chat['query'][:30]}", key=chat["id"]):
                st.session_state['load_query'] = chat["query"]
        st.sidebar.markdown("---")
        st.sidebar.write("Upload files, view saved sessions, and chat.")
    else:
        st.sidebar.info("Login or Signup to save your sessions.")

def top_auth_bar():
    if not st.session_state.get("logged_in", False):
        if st.session_state.get("show_auth_modal", False):
            auth.manage_auth()
        else:
            if st.button("Login / Signup"):
                st.session_state.show_auth_modal = True

def save_uploaded_file(uploaded_file):
    save_dir = "data/user_files"
    os.makedirs(save_dir, exist_ok=True)
    file_path = os.path.join(save_dir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path

def main_interface():
    st.title("Your Smart AI Study Buddy")
    sidebar_user_panel()
    top_auth_bar()

    logged_in = st.session_state.get("logged_in", False)
    if "anon_session_id" not in st.session_state:
        st.session_state["anon_session_id"] = str(uuid.uuid4())
    user_id = st.session_state.get("user_id") if logged_in else st.session_state["anon_session_id"]

    load_query = st.session_state.get('load_query', "")
    uploaded_file = st.file_uploader("Upload your study material (PDF or TXT)", type=["pdf", "txt"])
    query = st.text_input("Ask about a topic or enter your question here",
                          value=load_query if load_query else "")

    detail_level = st.selectbox("Select detail level", options=["Brief summary", "Detailed explanation"])

    if st.button("Get Summary") and query:
        if uploaded_file:
            file_path = save_uploaded_file(uploaded_file)
            rag.add_user_document(user_id, file_path)
            st.success("File uploaded and indexed!")

        user_docs = rag.search_similar(user_id, query)
        web_search_result = f"Simulated web info about {query}"
        combined_context = "\n\n".join(user_docs + [web_search_result])

        answer = llm.generate_summary(combined_context,
                                      "detailed" if detail_level == "Detailed explanation" else "brief")

        st.markdown("### Answer")
        st.write(answer)
        if logged_in:
            db.save_chat(user_id, query, answer)
        st.session_state['load_query'] = ""

if __name__ == "__main__":
    main_interface()
