# Import the load_dotenv function from dotenv
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Access the environment variables
BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_SECRET_KEY = os.getenv("BINANCE_SECRET_KEY")
FROM_MAIL = os.getenv("FROM_MAIL")
TO_MAIL = os.getenv("TO_MAIL")
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
