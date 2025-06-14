import os
from google.genai import types

def write_file(working_directory: str, file_path: str, content: str) -> str:
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(abs_file_path):
        try:
            os.makedirs(os.path.dirname(abs_file_path), exist_ok=True)
        except Exception as e:
            return f'Error creating directory {file_path}: {e}'
    
    #overwrite contents of the file path with content parameter
    if os.path.exists(abs_file_path) and os.path.isdir(abs_file_path):
            return f'Error: "{file_path}" is a directory, not a file'

    try:
        with open(abs_file_path, "w") as f:
            f.write(content)
        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )
    except Exception as e:
        return f"Error: writing to file: {e}"

     


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

