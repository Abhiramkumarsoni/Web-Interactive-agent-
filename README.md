🧠 Web Interactive Agent – AI-Powered Document Q&A App
An intelligent and interactive web application that allows users to upload documents or input web URLs and then ask questions in natural language about the content. Built using Streamlit, HuggingFace embeddings, Groq LLMs, and LangChain, this app acts like a private ChatGPT trained only on your custom input.

🔍 Problem Statement
Accessing knowledge from large documents or online content can be time-consuming. This project simplifies that by allowing users to chat with any document or webpage, asking specific questions and getting instant, accurate responses — like having your own AI-powered research assistant.

🚀 Key Features
✅ Upload a .txt file or provide a URL
✅ Automatically extract and preprocess text from the source
✅ Split documents into manageable chunks for context retention
✅ Convert text to embeddings using HuggingFace MiniLM
✅ Store vectors using FAISS for fast similarity search
✅ Use Groq’s LLaMA3 models to generate high-quality, context-aware answers
✅ Clean, interactive UI with Streamlit
✅ Optional: Sidebar model selector and Groq API key entry

🛠️ Tech Stack
Layer	Technology
Web Interface	Streamlit
Embeddings	HuggingFace Transformers (MiniLM-L6-v2)
Vector Store	FAISS
LLM Inference	Groq API (llama3-70b-8192)
Text Splitting	LangChain RecursiveCharacterTextSplitter
Content Loader	LangChain WebBaseLoader

📦 How It Works
User Uploads Document / Enters URL
→ Text is extracted from uploaded .txt file or scraped from webpage.

Text Preprocessing
→ Long documents are split into smaller chunks for better context handling.

Embedding Generation
→ Each chunk is converted into vector representation using all-MiniLM-L6-v2.

Semantic Search
→ FAISS searches for the most relevant chunks based on the user's query.

Question Answering
→ The relevant chunks are passed to Groq's LLaMA3 model to generate answers.

Streamlit Interface
→ Displays answer in an intuitive and responsive UI.

💡 Use Cases
📚 Research assistance: Summarize and query articles

📄 Document QA: Ask questions about custom reports or contracts

📰 News analysis: Understand key insights from blog or news articles

📊 Personal assistant: Chat with any structured text

🧪 Demo
🔑 Requires a Groq API key
pip install -r requirements.txt
streamlit run app.py

