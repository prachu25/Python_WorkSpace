from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Create Gemini client using API key
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        
        # System_Instaruction ->  Set the AI's role and behavior
        system_instruction="You are a teacher in a primary school. Help the students learn in the easiest way.",
    ),
    contents="Hello there"
)

print(response.text)