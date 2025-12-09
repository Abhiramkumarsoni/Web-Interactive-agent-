# 🧠 Web Interactive Agent – AI-Powered Document Q&A App

An intelligent web application that lets users upload documents or input web URLs and ask questions about the content using Natural Language. Built with **Streamlit**, **HuggingFace embeddings**, **Groq LLMs**, and **LangChain**, this app turns any document into an interactive AI assistant.

---

## 🔍 Problem Statement

Reading and extracting insights from lengthy documents or online content can be inefficient. This project provides an AI-powered interface to **chat with any document or webpage**, simplifying research and understanding.

---

## 🚀 Features

- 📄 Upload `.txt` files or provide a webpage URL  
- 🧠 Embedding generation using HuggingFace (`MiniLM-L6-v2`)  
- 🔍 Fast semantic search using FAISS  
- 🤖 Real-time response generation using **Groq LLaMA3** models  
- 🌐 Simple and responsive UI built with Streamlit  
- 🧩 Modular design with easy-to-extend components  

---

## 🛠 Tech Stack

| Component       | Technology Used                        |
|----------------|-----------------------------------------|
| Interface       | Streamlit                              |
| Embeddings      | HuggingFace (`all-MiniLM-L6-v2`)        |
| Vector Store    | FAISS                                   |
| LLM Backend     | Groq API (`llama3-70b-8192`)            |
| Chunking        | LangChain RecursiveCharacterTextSplitter |
| Loader          | WebBaseLoader for URL scraping          |

---

## 📦 How It Works

1. **Input**: Upload a `.txt` file or enter a URL  
2. **Load**: Extract content using `WebBaseLoader` or Streamlit’s file uploader  
3. **Split**: Divide content into smaller chunks  
4. **Embed**: Generate vector embeddings using HuggingFace  
5. **Search**: Use FAISS to retrieve relevant chunks based on query  
6. **Answer**: Pass retrieved content and query to Groq LLM for an answer  
7. **Display**: Show the response in the Streamlit UI

---

## 💻 How to Run Locally

1. **Install dependencies**  
    ```bash
    pip install -r requirements.txt
    ```

2. **Start the Streamlit app**  
    ```bash
    streamlit run app.py
    ```

3. **Enter your Groq API Key** in the sidebar  
4. Upload a text file or provide a URL  
5. Ask questions about the content 🎉

---

## 🔐 Requirements

- Python 3.8+
- Groq API Key (Get one at [https://console.groq.com](https://console.groq.com))

---

## 🧪 Use Cases

- 📰 Chat with news articles  
- 📊 Summarize and understand reports  
- 🧾 Read and interpret legal documents  
- 📚 Explore academic papers or research  

---

## 📸 Screenshots

![Screenshot 2025-06-28 112752](https://github.com/user-attachments/assets/b3052d95-9f8a-4fc5-a0da-ce23b691bda0)

