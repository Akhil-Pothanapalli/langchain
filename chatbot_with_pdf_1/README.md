# 📖 Langchain Document Question Answering using GPT 🤖

This project aims to convert a PDF document into text, process the text into chunks, and then use the GPT model to answer questions based on the document's content.

## 🛠️ Prerequisites

- Python 3.10 (Python 3.12 has been found to have issues ❤️)
- Pip

## 📦 Installation

Clone the repository and navigate to the project's root directory.

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

Install the required packages using pip and the provided requirements.txt file.

```bash
pip install -r requirements.txt
```

## 🧱 Key Components

- **PyPDF2**: Used to extract text from PDF documents.
- **Pandas**: Used for data manipulation and analysis.
- **Matplotlib**: Used for data visualization.
- **GPT2TokenizerFast**: Used to tokenize the text.
- **PyPDFLoader**: Used to load PDF documents.
- **RecursiveCharacterTextSplitter**: Used to split the text into chunks.
- **OpenAIEmbeddings**: Used to create text embeddings.
- **FAISS**: Used to create a vector database for similarity search.
- **ConversationalRetrievalChain**: Used to create a chain for question answering.

## 📝 Usage

1. Convert the PDF document to text using the `extract_text_from_pdf` function.
2. Save the extracted text to a .txt file and reopen it.
3. Create a function to count the tokens in the text using the GPT2TokenizerFast.
4. Split the text into chunks using the RecursiveCharacterTextSplitter.
5. Visualize the token count distribution using a histogram.
6. Create a vector database using the FAISS and OpenAIEmbeddings.
7. Perform a similarity search using the vector database to find the most relevant chunks for a given query.
8. Use the ConversationalRetrievalChain to generate an answer to the query based on the relevant chunks.

## 🚧 Current Issues and Future Work

- 🔄 The current version of OpenAI does not have the attribute "error". Therefore, it is necessary to downgrade to version 0.28 or use the OpenAI migrate option (https://github.com/openai/openai-python/discussions/742).
- 🛑 The current OpenAI rate limit has been reached. As a result, it is necessary to move to Google's Gemini. However, VertexAI has deprecated the VertexAIEmbeddings since 0.0.12.
- 💻 Python 3.12 has been found to have issues, so it is recommended to use Python 3.10 for this project ❤️.
- 🕰️ Due to these issues, the project will be halted for a while. The plan is to focus on something else and come back to this project later.

## 👏 Acknowledgments

- The Langchain team for their excellent work on document question answering ❤️.
- The OpenAI team for their powerful GPT model ❤️.
- The FAISS team for their efficient similarity search library ❤️.

🌟 Happy coding! 🌟 ❤️
