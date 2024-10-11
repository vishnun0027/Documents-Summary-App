from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Retrieve and set the Groq API key
groq_api_key = os.getenv("GROQ_API_KEY")
if groq_api_key is None:
    raise ValueError("GROQ_API_KEY not found in the environment variables.")
os.environ["GROQ_API_KEY"] = groq_api_key

from langchain_groq import ChatGroq

# Initialize the ChatGroq model with the specified model
llm = ChatGroq(model="llama3-8b-8192")
