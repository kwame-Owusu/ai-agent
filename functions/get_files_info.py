import os


def get_files_info(working_directory, directory=None):
    if directory not in working_directory:
        return f"Error: Cannot list '{directory}' as it is outside the permitted working directory"

    if not os.path.isdir(directory):
        return f"Error:  '{directory}' is not a directory"
    

    current_dir = os.listdir(working_directory)

    for item in current_dir:
        try:
            print(f"-{item}: file_size={os.path.getsize(item)}, is_dir={os.path.isdir(item)}")
        except:
            print("Error occured in getting stats for items in directory") 
