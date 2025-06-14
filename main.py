import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import Client, types


 
def main() -> None:
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)
       
    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]
    user_prompt = " ".join(args) 
    if not args:
        print("AI Code Assistant")
        print("\nUsage: python main.py 'your prompt here'")
        print("Example:  python main.py 'How do i build a calculator' ")
        sys.exit(1)

    messages = [ types.Content(role="user", parts=[types.Part(text=user_prompt)]), ]
    generate_content(client, messages, verbose)
    if verbose:
        print(f"User prompt: {user_prompt}\n")



def generate_content(client: Client, messages: list, verbose: bool = False) -> None:
    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)
    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}") #type:ignore
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")#type:ignore
    print("Response:")
    print(response.text)




if __name__ == "__main__":
    main()

