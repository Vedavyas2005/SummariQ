import streamlit as st
from db import create_user, authenticate_user, get_user_id

def signup():
    st.subheader("Sign Up")
    username = st.text_input("Username", key="signup_username")
    password = st.text_input("Password", type='password', key="signup_password")
    if st.button("Sign Up"):
        if username and password:
            if create_user(username, password):
                st.success("Signup successful! Please login.")
                st.session_state.signup_done = True
            else:
                st.error("Username already exists.")
        else:
            st.error("Enter both username and password.")

def login():
    st.subheader("Log In")
    username = st.text_input("Username", key="login_username")
    password = st.text_input("Password", type='password', key="login_password")
    if st.button("Log In"):
        if authenticate_user(username, password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.user_id = get_user_id(username)
            st.success(f"Logged in as {username}")
        else:
            st.error("Invalid username or password.")

def logout():
    if st.button("Log Out"):
        st.session_state.clear()
        st.experimental_rerun()

def manage_auth():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "signup_done" not in st.session_state:
        st.session_state.signup_done = False

    if st.session_state.logged_in:
        st.write(f"Welcome, {st.session_state.username}!")
        logout()
    else:
        col1, col2 = st.columns(2)
        with col1:
            login()
        with col2:
            signup()
