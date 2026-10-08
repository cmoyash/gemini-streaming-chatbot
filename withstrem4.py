import os
from google import genai
from dotenv import load_dotenv


load_dotenv()
api_key=os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("Api Key Not Found")

client=genai.Client(
    api_key=api_key
)

system_prompt="""
1. Be polite
2. Be proffesional
3. Be Helpful
4. Rember all previous chat as context
5. You are a friendly AI assistant.
"""

History=[]
MAX_HISTORY=20



print(("=="*50))
print("YASH'S PERSONAL CHATBOT")
print(("=="*50))

while True:
    user_input=input("\nEnter Prompt: ")
    if not user_input:
        print("Enter The Prompt !!")
        continue
    if user_input.lower() in ["bye" , "exit" , "stop"]:
        print("Bye Have A Great Time (:")
        break

    History.append(f"User: {user_input}")
    Convo_context=system_prompt+ ("\n")
    Convo_context+=("\n").join(History)
    try:
        stream=client.models.generate_content_stream(
            model="gemini-3.5-flash-lite" ,
            contents=Convo_context
        )
        main_responce=""
        for chunks in stream:
            if chunks.text:
                print(chunks.text , end="" , flush=True)
                main_responce+=chunks.text

        History.append(f"Gemini: {main_responce}")
        History=History[-MAX_HISTORY:]
    except Exception as e:
        print(f"Error: {e}")
        History.pop()
