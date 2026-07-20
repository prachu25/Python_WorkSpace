from google import genai
import os                        # Used to access environment variables
from dotenv import load_dotenv   # Loads variables from the .env file
from google.genai import types

# Load .env file
load_dotenv()

# Read API Key
api_key = os.getenv("GEMINI_API_KEY")

# create client
client = genai.Client(api_key = api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="How does Ai work, give me short 4 in line?",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=0) # Disables thinking
    ),    # Model will answer without thinking
)

print(response.text)