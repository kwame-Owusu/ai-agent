import os

MAX_CHARS = 10000

def get_file_content(working_directory, filepath):
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = abs_working_dir

    if not filepath.startswith(target_dir):
        return f'Error: Cannot read "{filepath}" as it is outside the permitted working directory'

    if not os.path.isfile(filepath):
        return f'Error: File not found or is not a regular file "{filepath}" '

    
    try:
        with open(filepath, "r+") as file:
            if len(file.read()) > MAX_CHARS:
                file.truncate(MAX_CHARS)
                file.write(f"File '{file}' truncated at 10000 characters")
            else:
                file_content = file.read(MAX_CHARS)
                return file_content

    except Exception as e:
        return f"Error: trouble reading file {e}"




