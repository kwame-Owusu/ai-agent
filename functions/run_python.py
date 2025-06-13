import os
import subprocess
import time


def run_python(working_directory, filepath):
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
        completed_process = subprocess.run(abs_file_path)
        time.sleep(30) #to prevent infinite execution
        std_out = completed_process.stdout
        std_err = completed_process.stderr
        output = f"STDOUT: {std_out}\nSTDERR: {std_err}" 

        if completed_process.returncode != 0:
            output += f" Process exited with code {completed_process.returncode}" 
        else:
            return "No output produced"

        return output

    except Exception as e:
        return f"Error: executing Python file: {e}"

    






