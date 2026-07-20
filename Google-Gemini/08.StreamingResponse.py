from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key = api_key)

response = client.models.generate_content_stream(
    model = "gemini-2.5-flash",
    contents=['How cricket is played?']
)

for chunk in response:
    print(chunk.text, end=" ")

"""
what is the chunk?

Instead of waiting for the entire answer, Gemini sends the response piece by piece.
Each piece is called a chunk.
"""