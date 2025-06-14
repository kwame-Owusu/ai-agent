import os
import subprocess

from google.genai import types

def run_python_file(working_directory: str, filepath: str) -> str:
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, filepath))

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{filepath}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        return f'Error: File "{filepath}" not found'
    if not abs_file_path.endswith(".py"):
        return f'Error: "{filepath}" is not a python file'

    #use subprocess to run to execute the python file
    try:
         # Run Python file with proper interpreter and capture output
        completed_process = subprocess.run(
            ['python3', abs_file_path],  # Use python3 explicitly
            capture_output=True,         # Capture stdout and stderr
            text=True,                   # Return strings instead of bytes
            timeout=30,                  # Prevent infinite execution
            cwd=abs_working_dir          # Set working directory
        )
        output = f"STDOUT:\n{completed_process.stdout}\nSTDERR:\n{completed_process.stderr}"
    
        if completed_process.returncode != 0:
            output += f"Process exited with code {completed_process.returncode}" 

        if not completed_process.stdout.strip() and not completed_process.stderr.strip():
            output += "\nNo output produced"
    
        return output

    except Exception as e:
        return f"Error: executing Python file: {e}"


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


