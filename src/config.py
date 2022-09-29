import os
from dotenv import load_dotenv

load_dotenv()

APP_PORT = os.getenv('APP_PORT')
