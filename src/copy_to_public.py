import os
import shutil


def copy_to_public(source, destination):
    if not os.path.exists(destination):
        os.mkdir(destination)

    for entry in os.listdir(source):
        current_path = os.path.join(source, entry)
        if os.path.isfile(current_path):
            shutil.copy(current_path, destination)
        else:
            new_directory = os.path.join(destination, entry)
            copy_to_public(current_path, new_directory)

