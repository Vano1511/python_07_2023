from randoms import random_name as rn
from pathlib import Path
from random import choice, randint

ext = ["txt", "vid", "mov", "mp3", "msc", "pic", "row", "ico", "ukn"]


def create_files(extensions: list, directory: str, files_count: int):
    """Create new files with random names and extensions."""\

    try:
        Path.mkdir(directory)
    except FileExistsError:
        pass
    for i in range(files_count):
        file_name = f"{rn(max_chr=10).lower()}.{choice(extensions)}"
        path = Path.cwd() / "dir" / file_name
        try:
            with open(path, "x", encoding="utf_8") as file:
                file.write(rn(max_chr=30))
        except FileExistsError:
            pass


if __name__ == "__main__":
    create_files(ext, "dir", randint(1, 6))
