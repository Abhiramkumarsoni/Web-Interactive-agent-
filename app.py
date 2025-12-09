import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_groq import ChatGroq
from langchain.schema import Document

st.set_page_config(page_title="Web Interactive Agent", layout="wide")
st.title("🧠 Web Document Q&A App")

# Sidebar API Key Input
groq_api_key = st.sidebar.text_input("Enter your Groq API Key", type="password")
url_input = st.text_input("Enter a Web URL (optional):")
uploaded_file = st.file_uploader("Or upload a text-based file (.txt)", type=["txt"])

if (uploaded_file or url_input) and groq_api_key:
    if url_input:
        st.info("Fetching content from URL...")
        loader = WebBaseLoader(url_input)
        documents = loader.load()
    else:
        text = uploaded_file.read().decode("utf-8")
        documents = [Document(page_content=text)]

    # Split text
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(documents)

    # Embeddings
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(chunks, embeddings)

    # Chat setup (✔ fixed)
    groq_llm = ChatGroq(
        groq_api_key=groq_api_key,
        model="llama-3.1-8b-instant"
    )

    chain = load_qa_chain(groq_llm, chain_type="stuff")

    query = st.text_input("Ask a question about the content:")

    if query:
        relevant_docs = vectorstore.similarity_search(query)
        answer = chain.run(input_documents=relevant_docs, question=query)

        st.write("### 🤖 Answer:")
        st.success(answer)

else:
    st.warning("Please enter a Groq API key and provide a URL or upload a file.")
