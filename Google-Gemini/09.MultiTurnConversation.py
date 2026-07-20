import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key = api_key)

chat = client.chats.create(model="gemini-2.5-flash")

print("Gemini Chat Started!")
print("Type 'exit' to end the chat.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bye!")
        break
    
    response = chat.send_message(user_input)

    print("Gemini: ", response.text)
    print()

