import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import Client, types

def main() -> None:
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)
       
    args = sys.argv[1:] 
    if not args:
        print("AI Code Assistant")
        print("\nUsage: python main.py 'your prompt here'")
        print("Example:  python main.py 'How do i build a calculator' ")
        sys.exit(1)

    user_prompt = " ".join(args) 
    messages = [ types.Content(role="user", parts=[types.Part(text=user_prompt)]), ]
    generate_content(client, messages)



def generate_content(client: Client, messages: list) -> None:
    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)
    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()

