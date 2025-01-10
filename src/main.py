import os
import shutil
from copy_to_public import copy_to_public
from generate_page import generate_page



source = "./static"
destination = "./public"


def main():
    print("Deleting public directory...")
    if os.path.exists(destination):
        shutil.rmtree(destination)

    print("Copying static files to public directory...")
    copy_to_public(source, destination)
    print(f"Files copied successfully!")

    generate_page("./content/index.md", "./template.html", "./public/index.html")

    
main()

