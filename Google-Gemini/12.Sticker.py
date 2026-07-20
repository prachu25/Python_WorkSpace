import os
from google import genai
from dotenv import load_dotenv
from google.genai import types

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key = api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash-image",
    contents= "A kawaii-style sticker of a happy red panda wearing a tiny bamboo hat. It's munching on a green bamboo leaf. " \
    "The design features bold, clean outlines, simple cel-shading, and a vibrant color palette. The background must be white.",
)

for part in response.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = part.as_image()
        image.save("red_pandas_sticker.png")