import os

def returnPosts():
    # Directory path
    directory_path = "pages"

    # Check if the directory exists
    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        # Get the list of file names in the "pages" directory
        my_list = os.listdir(directory_path)

        #remove src and homepage from array
        strings_to_remove = ["homepage.html", "src"]
        my_list = [item for item in my_list if item not in strings_to_remove]

        return my_list
    else:
        print(f"The '{directory_path}' directory does not exist in the current working directory.")


if __name__ == "__main__":
    post_list = returnPosts()
    post_list_split = []
    for i in range(len(post_list)):
        post_list_split.append(post_list[0].split('_'))
    print(post_list_split)