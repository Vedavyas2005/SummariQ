# SummariQ: Gemini-Powered Study Assistant

SummariQ is a modern, AI-powered study companion that transforms your study materials into instant, high-quality summaries and explanations. Upload PDFs, TXT files, or simply ask questions—SummariQ uses Google's Gemini LLM and advanced Retrieval-Augmented Generation (RAG) to deliver contextual, tailored answers based on your own notes or public topics.

# Try it out at: 
https://summariq-qh2pnj4w3clsto67zcgado.streamlit.app/

## ✨ Key Features
Multimodal Summarization: Upload your lecture notes or reference PDFs and get concise or detailed summaries instantly.

RAG-Powered Q&A: Ask questions about your own uploaded materials or any topic; SummariQ retrieves the most relevant chunks to answer with clarity.

Gemini AI Integration: Leverages Google's Gemini LLM for human-like, adaptive explanations, so you always get content that's easy to understand.

User Accounts & Session Tracking: Simple signup/login system keeps your chat history and uploaded files organized.

Anonymous Access: Use all summarization features even without an account—great for quick research or guests.

Streamlit UI: Intuitive, modern interface with Perplexity-style chat and session panels, optimized for web and mobile.

##🚀 Tech Stack
Streamlit: For fast, rich web app UI and deployment.

Google Gemini API: For state-of-the-art LLM summaries and explanations.

ChromaDB & Sentence-Transformers: Vector storage and retrieval for contextual document understanding.

SQLite: Lightweight database for user data and session history.

# ⚡ How It Works
Upload your PDFs or TXT files on the app.

Ask any question or topic relevant to your material.

SummariQ searches your documents (using vector similarity), builds context, and sends it to Gemini for final summarization.

View clean answers, revisit chat history, and learn—all in one place.

# 🛠️ Getting Started
Clone the repo and set your Gemini API key.

Install dependencies from requirements.txt.

Run locally with Streamlit, or deploy instantly to Streamlit Cloud.

# 💡 Why SummariQ?
Whether you're a student, researcher, or lifelong learner, SummariQ makes studying more efficient, interactive, and personalized. No more generic search! Get summaries and explanations crafted just for your own notes and resources.

# 📄 License
MIT License — free for students, educators, and makers!

Feel free to fork, star, and contribute! If you have questions or want to add features (like S3 storage, real-time web search, or more file types), open an issue or discussion. Happy summarizing!

# Issues
No permanent Storage for User Accounts or Files, it's all session managed via Streamlit. Until the app is running the storage is saved securely. In FUTURE UPDATES will migrate everything to a more permanent Cloud Storage.
