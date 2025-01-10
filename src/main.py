import os
import shutil
from copy_to_public import copy_to_public
from generate_page import generate_pages_recursive



source = "./static"
dest_path = "./public"
content_path = "./content"
template_path = "./template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(dest_path):
        shutil.rmtree(dest_path)

    print("Copying static files to public directory...")
    copy_to_public(source, dest_path)
    print("Files copied successfully!")

    print("Generating content...")
    generate_pages_recursive(content_path, template_path, dest_path)
    print("Done!")

    
main()

