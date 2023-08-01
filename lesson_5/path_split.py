import os

file_path = "F:\учеба\python_07_2023\lesson_5\path_split.py"


def file_from_path(path_: str) -> tuple:
    """Recieve absolute path to file and returns tuple(path, file_name, file_extention)."""

    head, file = os.path.split(path_)
    file_name, file_extention = file.split(".")
    return os.path.join(head), file_name, file_extention


print(file_from_path(file_path))
