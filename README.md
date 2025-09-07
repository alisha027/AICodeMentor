# 🚀 **AI Code Mentor**

An AI-powered multi-agent system that acts as your personal coding mentor. It helps in **debugging, error correction, explanation, and answering programming-related queries**.

🔗 **Live Demo:** [AI Code Mentor Streamlit App](https://aicodementor-74kskbuwjxmrjaymzrwnea.streamlit.app/)
📂 **GitHub Repository:** [AI Code Mentor](https://github.com/alisha027/AICodeMentor)

---

## 📌 **Problem Statement**

Debugging and understanding code errors is one of the most time-consuming tasks for developers, especially beginners.

Programmers often struggle with:

* Identifying syntax, logical, or runtime errors
* Understanding why an error occurred
* Learning how to write optimized and correct code

**AI Code Mentor** solves this by acting as an **intelligent coding assistant** that not only fixes errors but also **explains the reasoning behind the solution**.

---

## 🤖 **Multi-Agent System Design**

AI Code Mentor uses multiple AI agents working independently and collaboratively:

1. **Error Detection Agent** – Scans code and identifies errors
2. **Correction Agent** – Suggests fixes while keeping the intended logic
3. **Explanation Agent** – Explains why errors occurred and how the fix works
4. **Query Response Agent** – Answers general coding questions and provides examples

This **multi-agent approach** ensures users don’t just get corrected code, but also understand *why* and *how* it works.

---

## 🛠️ **Tools, Libraries, and Frameworks**

* **Python** – Core language for implementation
* **Streamlit** – Interactive frontend for the application
* **Ollama** – For running and hosting the LLM
* **Ngrok** – Tunneling to expose the local server to the internet
* **DeepSeek-Coder:6.7b** – LLM specialized in programming tasks
* **Requests & JSON** – For API calls and communication

---

## 🧠 **LLM Selection**

The project uses **DeepSeek-Coder:6.7b**, an open-source large language model optimized for programming tasks.

### ✅ **Why DeepSeek-Coder:6.7b?**

* Excellent **code comprehension and debugging** skills
* Generates **clean and optimized code**
* Provides **context-aware explanations** in natural language
* **Open-source** and resource-efficient (good balance between performance and hardware requirements)

This makes it the **ideal choice** for building a real-time AI mentor system.

---

## 🚀 **Deployment**

* **GitHub Repo:** [AI Code Mentor](https://github.com/alisha027/AICodeMentor)
* **Live Demo (Streamlit):** [Try it here](https://aicodementor-74kskbuwjxmrjaymzrwnea.streamlit.app/)

---
⚙️ Installation & Setup

Follow these steps to set up and run the project:

1️⃣ Run Notebook in Google Colab

* Open aicodementor.ipynb in Google Colab

* Add your Ngrok Auth Token (from ngrok.com
) inside the notebook

* Run all cells → this will generate a public OLLAMA link

2️⃣ Update app.py

* Copy the Ngrok link from Colab

* Open app.py

* Replace the placeholder URL with your new OLLAMA link

3️⃣ Install Dependencies

* pip install -r requirements.txt


4️⃣ Run the Streamlit App

* streamlit run app.py


✅ Your AI Code Mentor app will now be live 🎉


## ✨ **Features**

* ✅ Detects and fixes code errors
* ✅ Explains why errors occurred
* ✅ Provides optimized solutions
* ✅ Acts as a coding mentor, not just a debugger
* ✅ Simple and interactive UI

---

## 👩‍💻 **Author**

**Alisha Vashisht**
📧 Email: [vashishtalisha02@gmail.com](mailto:vashishtalisha02@gmail.com)

---

🔥 With **AI Code Mentor**, debugging and learning programming becomes **faster, easier, and smarter**!
