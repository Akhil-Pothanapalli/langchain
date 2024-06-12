# 📦 Langchain Demo with Google Generative AI and Gemma:2b

This repository contains two driver codes for the Langchain Demo:

1. 🧪 `app.py` - A Streamlit-based application that uses the Google Generative AI API (Gemini) to generate responses to user queries.
2. 🦙 `locallm.py` - A Streamlit-based application that uses the Ollama language model (Gemma:2b) to generate sarcastic and funny responses to user queries.

## 💾 Installation

1. Clone the repository:
```
git clone https://github.com/your_username/langchain_demo.git
```
1. Navigate to the cloned repository:
```bash
cd langchain_demo
```
1. Create a virtual environment (optional but recommended):
```
python -m venv venv
```
1. Activate the virtual environment:

On Windows:
```powershell
.\venv\Scripts\activate
```
On macOS/Linux:
```bash
source venv/bin/activate
```
1. Install the required packages:
```bash
pip install -r requirements.txt
```
1. Create a `.env` file in the root directory of the project and add the following environment variables:
```makefile
GOOGLE_API_KEY=your_google_api_key
LANGCHAIN_API_KEY=your_langchain_api_key
```
Replace `your_google_api_key` and `your_langchain_api_key` with your actual API keys.

## 🚀 Usage

To run the `app.py` application, navigate to the root directory of the project and execute the following command:
```bash
streamlit run app.py
```
This will launch the Streamlit application in your default web browser.

To run the `locallm.py` application, navigate to the root directory of the project and execute the following command:
```bash
streamlit run locallm.py
```
This will launch the Streamlit application in your default web browser.

## 🙋‍♂️ Acknowledgments

- The Google Generative AI API (Gemini) for providing high-quality language generation capabilities.
- The Ollama language model (Gemma:2b) for providing sarcastic and funny language generation capabilities.
- The Streamlit framework for making it easy to create interactive web applications.
