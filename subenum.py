import requests
import os 
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("security-trail-key")
print("key:",api_key)