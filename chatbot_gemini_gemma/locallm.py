from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

##Prompt template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are friend who talks informally, sarcastic and funny manner. Please respond to the user queies"),
        ("user","Question:{question}")
    ]
)

## streamlit framework

st.title("Langchain demo with Gemma:2b")
input_text = st.text_input("Ask your sarcastic buddy")

## Gemini Gemma:2b
llm = Ollama(model="gemma:2b")
output_parser=StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))
