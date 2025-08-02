import streamlit as st
from pdf_handler import extract_text_from_pdf, chunk_text
from vector_search import get_embeddings, create_faiss_index, search_similar_chunks
from LLM_response import generate_response

st.set_page_config(page_title="StudyMate - Smart PDF Q&A", layout="centered")

st.title("📚 StudyMate - Smart PDF Q&A")

pdf = st.file_uploader("📄 Upload a PDF", type="pdf")

if pdf:
    with st.spinner("🔍 Extracting text..."):
        text = extract_text_from_pdf(pdf)
        text_chunks = chunk_text(text)
    
    with st.spinner("🧠 Generating embeddings..."):
        embeddings = get_embeddings(text_chunks)
        index = create_faiss_index(embeddings)

    user_question = st.text_input("❓ Ask a question about the PDF:")

    if user_question:
        with st.spinner("🔎 Finding relevant content..."):
            relevant_chunks = search_similar_chunks(user_question, text_chunks, index)
            context = " ".join(relevant_chunks)

        with st.spinner("🤖 Generating answer..."):
            prompt = f"Context: {context}\n\nQuestion: {user_question}\nAnswer:"
            response = generate_response(prompt)

        st.subheader("📝 Answer")
        st.write(response)
