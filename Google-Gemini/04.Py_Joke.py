from google import genai
import os                        # Used to access environment variables
from dotenv import load_dotenv   # Loads variables from the .env file

# Load .env file
load_dotenv()

# Read API Key
api_key = os.getenv("GEMINI_API_KEY")    # Read the API key securely from the .env file

# create client
client = genai.Client(api_key = api_key)

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="""
Generate a short joke about Python programmers.
Language: Hinglish (Hindi + English)
Length: Exactly 3 lines.
Make it funny and end with a punchline.
"""
)

print("\n")
print(response.text)
print()