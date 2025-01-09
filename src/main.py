import os
import shutil
from copy_to_public import copy_to_public



source = "./static"
destination = "./public"


def main():
    if os.path.exists(destination):
        shutil.rmtree(destination)

    copy_to_public(source, destination)


    
main()

