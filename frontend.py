import streamlit as st
import requests

# FastAPI backend URL
BACKEND_URL = "http://localhost:8000"

st.title("Document Query System")

# File Upload
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file:
    # Send the file to the backend
    files = {"file": uploaded_file.getvalue()}
    response = requests.post(f"{BACKEND_URL}/upload/", files=files)
    if response.status_code == 200:
        st.success("File uploaded successfully!")
    else:
        st.error("Failed to upload the file!")

    # Query Input
    query = st.text_input("Ask a question about the document:")

    if query:
        response = requests.get(f"{BACKEND_URL}/query/", params={"query": query})
        if response.status_code == 200:
            st.write("Answer:", response.json()["answer"])
        else:
            st.error("Failed to get an answer!")

    # Summarize Button
    if st.button("Summarize Document"):
        response = requests.get(f"{BACKEND_URL}/summarize/")
        if response.status_code == 200:
            st.write("Summary:", response.json()["summary"])
        else:
            st.error("Failed to get a summary!")
