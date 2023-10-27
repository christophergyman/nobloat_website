import os

# Directory path
directory_path = "pages"

# Check if the directory exists
if os.path.exists(directory_path) and os.path.isdir(directory_path):
    # Get the list of file names in the "pages" directory
    file_names = os.listdir(directory_path)
    print("File names in the 'pages' directory:")
    print(file_names)
else:
    print(f"The '{directory_path}' directory does not exist in the current working directory.")

