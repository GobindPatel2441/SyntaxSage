from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()
def load_llm():
    llm = ChatGroq(
        groq_api_key = os.getenv('api_key'),
        model_name = "llama-3.3-70b-versatile",
        temperature= 0.5
    )
    return llm