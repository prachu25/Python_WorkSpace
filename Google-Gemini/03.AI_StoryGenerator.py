from google import genai
from gtts import gTTS
import os

client = genai.Client(api_key="YOUR_API_KEY")

topic = input("Story Topic: ")

prompt = f"""
Write a short fantasy story in Hindi on the following topic:

{topic}

Return only the story in Hindi.
"""

response = client.models.generate_content(
    model="gemini-flash-latest",
    contents=prompt
)

story = response.text

print(story)

tts = gTTS(text=story, lang="hi")

tts.save("story.mp3")

os.startfile("story.mp3")
