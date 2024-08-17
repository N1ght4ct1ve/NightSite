# from dotenv import load_dotenv
import secrets
import os

# load_dotenv()

class Config:
    # SECRET_KEY = os.getenv('SECRET_KEY')
    SECRET_KEY = secrets.token_hex(32)
    
