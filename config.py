import os 
from dotenv import load_dotenv
load_dotenv()
class Config:
    api_key = os.getenv("api_key")