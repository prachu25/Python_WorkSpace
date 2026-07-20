import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

#create gemini client
client = genai.Client(api_key = api_key)

prompt = input("Enter your image prompt: ")

print("\n Generating image... Please wait. \n")

# Generate image from text
response = client.models.generate_content(
    model = "gemini-2.5-flash-image",
    contents =[prompt]
)

# process the response
for part in response.parts:

    # print text response (if any)     print.text - print the text
    if part.text is not None:
        print(part.text)

    # save generated image      part.inline_data  Convert to image & save
    elif part.inline_data is not None:
        image = part.as_image()
        image.save("generated_image.png")
        print("Image Saved as 'generated_image.png")