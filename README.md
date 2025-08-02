# StudyMate
# 📄 StudyMate – Ask Questions from PDF Using AI

StudyMate is an AI-powered PDF question-answering tool. Upload any PDF file (like lecture notes, articles, or books) and ask questions about its content. The system uses Natural Language Processing (NLP) and Large Language Models (LLMs) to understand the document and provide answers.

## 🚀 Features

- 📄 Upload any PDF file
- 💬 Ask questions about the content
- 🧠 Uses a Hugging Face transformer model (like bert-base-uncased or distilbert)
- 🌐 Simple interface for interaction

---

## 🛠 Tech Stack

- Python
- Streamlit (for web UI)
- PyMuPDF / pdfminer / PyPDF2 (for PDF reading)
- Hugging Face Transformers (for QA model)
- Langchain or Sentence Transformers (optional for embedding)
- dotenv (for safely using API keys)

---

## 🖥 How It Works

1. Upload a PDF file.
2. The content is extracted and split into chunks.
3. You type a question.
4. The system finds the most relevant chunk and answers your question using a language model.

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/StudyMate.git
cd StudyMate
