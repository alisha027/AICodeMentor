# app.py
import streamlit as st
import requests
import json

# ---------------------------
# Configuration
# ---------------------------
OLLAMA_URL = "https://6c4dfa764afd.ngrok-free.app/api/generate"  # Replace with your ngrok URL

# ---------------------------
# Query Function
# ---------------------------
def ask_model(prompt: str):
    payload = {
        "model": "deepseek-coder:6.7b",
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(
            OLLAMA_URL,
            headers={"Content-Type": "application/json"},
            data=json.dumps(payload)
        )
        if response.status_code == 200:
            return response.json()["response"]
        else:
            return f"❌ Error {response.status_code}: {response.text}"
    except Exception as e:
        return f"⚠️ Exception: {str(e)}"

# ---------------------------
# Custom Styling
# ---------------------------
st.set_page_config(page_title="AI Code Mentor", page_icon="🤖", layout="wide")

st.markdown("""
    <style>
    body {
        background-color: #f0f8ff;
    }
    .main-title {
        font-size: 36px;
        font-weight: bold;
        text-align: center;
        color: #1e90ff;
        margin-bottom: 20px;
            }
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #00c853;  /* Bright green like your code snippet */
        margin-bottom: 40px;
        font-weight: 500;
    }

    .stTextArea textarea {
        border-radius: 12px;
        border: 2px solid #2E86C1;
        background-color: #ffffff;
        font-size: 16px;
        color: #000000;
    }
    .stButton>button {
        background-color: #2E86C1;
        color: white;
        font-size: 16px;
        border-radius: 12px;
        padding: 8px 16px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #1A5276;
    }
    .answer-box {
        background-color: #EBF5FB;  /* Light blue background */
        padding: 16px;
        border-radius: 12px;
        border-left: 6px solid #2E86C1;
        font-size: 16px;
        color: #1B2631;  /* Dark text for contrast */
    }
    </style>
""", unsafe_allow_html=True)


# ---------------------------
# Layout
# ---------------------------
st.markdown("<div class='main-title'>🤖 AI Code Mentor</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Your friendly coding buddy — ask me anything about Python, Java, debugging, or logic! 🧑‍💻</div>", unsafe_allow_html=True)

# Input area
user_input = st.text_area("💬 Enter your coding question below:", height=120, placeholder="e.g. Why do I get 'IndentationError' in Python?")

col1, col2 = st.columns([1, 3])

with col1:
    ask_btn = st.button("🚀 Ask Mentor")

with col2:
    st.markdown("""
    **💡 Example Questions for You:**
    - Why do we use loops in coding? 🔁
    - Can you debug this code: `def add(a b): return a+b` ❓
    - Explain recursion like I’m 15 📚
    """)

# Response
if ask_btn:
    if user_input.strip() == "":
        st.warning("✍️ Please enter a question before clicking Ask!")
    else:
        with st.spinner("🧠 Thinking hard..."):
            answer = ask_model(user_input)
        st.markdown("### 📝 Mentor's Answer:")
        st.markdown(f"<div class='answer-box'>{answer}</div>", unsafe_allow_html=True)
