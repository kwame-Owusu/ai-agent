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
    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

        - List files and directories

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """
    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages, config=types.GenerateContentConfig(
        tools=[available_functions], system_instruction=system_prompt))
    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}") #type:ignore
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")#type:ignore

    print("Response:")
    if response.function_calls:
        for func in response.function_calls:
            print(f"Calling function {func.name}({func.args})")
    else:
        print(response.text)




schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads and returns the content of a specified file, constrained to the working directory. Content is limited to 10,000 characters and will be truncated if longer.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="The base working directory path that constrains file access.",
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to read, relative to the working directory.",
            ),
        },
        required=["working_directory", "file_path"],
    ),
)


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="The base working directory path that constrains file access.",
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="the path of the file where content is going to be written",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="the content that is going to be written into the file",
            ),

        },
        required=["working_directory", "directory", "content"],  

    ),
)

schema_run_python_file = types.FunctionDeclaration(
    name="write_file",
    description="runs a python file in a specified filepath, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="The base working directory path that constrains file access.",
            ),
            "filepath": types.Schema(
                type=types.Type.STRING,
                description="where the file is and is going to be executed",
            ),
        },
        required=["working_directory", "filepath"],  
    ),
)

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
    ]
)


if __name__ == "__main__":
    main()

