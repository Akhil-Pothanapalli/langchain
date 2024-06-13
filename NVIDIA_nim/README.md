
📄 **Project: NVIDIA NIM Demo**

🔧 **Tech Stack**
- os
- langchain_nvidia_ai_endpoints
- langchain_community
- PyPDFDirectoryLoader
- RecursiveCharacterTextSplitter
- FAISS
- streamlit
- dotenv

📥 **Data Ingestion**
The data is ingested using `PyPDFDirectoryLoader` from the directory `./hindu_scriptures`.

🧩 **Text Splitting**
The text is split into chunks using `RecursiveCharacterTextSplitter` with a chunk size of 700 and a chunk overlap of 50.

🌐 **Vector Embedding**
The vector embedding is done using `NVIDIAEmbeddings` and the vectors are stored in `FAISS` for similarity search.

🤖 **Language Model**
The language model used is `ChatNVIDIA` with the model `meta/llama3-70b-instruct`.

🎛️ **User Interface**
The user interface is built using `streamlit`. The user can enter a question and the system will retrieve the most relevant answer from the documents.

🕰️ **Response Time**
The response time of the system is also calculated and displayed.

📄 **Document Similarity Search**
The system also provides an option to display the documents that are most similar to the question.

🚫 **NVIDIA Credits**
Please note that NVIDIA only provides 1000 credits for API usage. Once these credits are exhausted, a business email is required for further usage. Personal emails will not work.

🔜 **Future Work**
I've recently come across `OllamaEmbeddings` and I'm planning to use them in the future.

🚀 **How to Run**
1. Install the required packages.
2. Load the environment variables using `dotenv`.
3. Set the NVIDIA API key.
4. Run the code.
