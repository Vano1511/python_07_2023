from pathlib import Path
import os
import shutil

files_dict = {
    "Music": ["mp3", "msc"],
    "Text": ["txt", "row"],
    "Video": ["vid", "mov"],
    "Pictures": ["pic", "ico"]
}


def sort_files(extension_dict: dict):
    for directory, extensions in extension_dict.items():
        try:
            Path.mkdir(directory)
        except FileExistsError:
            pass
        p = Path.cwd() / "dir"
        for obj in p.iterdir():
            file_name = os.path.basename(obj)
            print(file_name)
            if obj.suffix[1:] in extensions:
                shutil.copy(obj, os.path.join(os.getcwd(), directory))
                os.remove(obj)

if __name__ == "__main__":
    sort_files(files_dict)
