from PIL import Image
from google import genai
import os
from dotenv import load_dotenv

# Load variables from the .env file
load_dotenv()

# Read the Gemini API key from the .env file
api_key = os.getenv("GEMINI_API_KEY")

# Create the Gemini client
client = genai.Client(api_key=api_key)

# Open the image
image = Image.open("instrument.jpg")

# Send the image and prompt to Gemini
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[
        image,
        "Tell me about this instrument in simple English in short way ."
    ]
)

# Display the AI response
print("\n Gemini Response:\n")
print(response.text)



"""
"Multimodal" = Ek AI jo sirf text hi nahi, balki image, audio,
 video jaise multiple formats ko bhi samajh sakta hai.

 EX:  contents=[image, "What is this instrument?"]
"""