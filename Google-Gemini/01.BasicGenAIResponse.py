# pip install google-genai

from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents="Write a java program to add two numbers, without extra information"
)

print(response.text)
