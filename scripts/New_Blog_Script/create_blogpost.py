import os

# Define the file paths
markdown_template_path = "markdown_template.html"
html_markup_path = "blog_template.html"

post_date = input("Date for post DD-MM-YYYY: ")
undercase = "_"
post_name = input("PostName (space = -): ")
html_string = ".html"

final_path = post_date + undercase + post_name + html_string

# Specify directory to place new file
# parent_dir = os.path.dirname(os.getcwd())
specified_dir = "/home/chezu/Documents/github/nobloat_website/pages"

# Create the new post file path in the specified directory 
new_post_path = os.path.join(specified_dir, final_path)

# Read the content of the markdown template file
with open(markdown_template_path, "r") as template_file:
    markdown_content = template_file.read()

# Read the content of the HTML markup file
with open(html_markup_path, "r") as markup_file:
    html_lines = markup_file.readlines()

# Insert the markdown content at line 57 (0-based index)
insert_line_number = 59  # Line 57 in a 0-based index
html_lines.insert(insert_line_number, markdown_content)

# Write the modified content to the new post file
with open(new_post_path, "w") as new_post_file:
    new_post_file.writelines(html_lines)
