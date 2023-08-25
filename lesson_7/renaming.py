from pathlib import Path


def renaming_files(wanted_name, count_nums=3, extension_old=".txt", extension_new=".csv", tolerance=[3, 6]):
    """Function renames files with old extension to new.
    recieve: wanted_name, count of digits, old and new extensions and tolerance to take part of old name"""

    def new_part(old_name, tolerance=tolerance):
        """cut part of old name depehds of tolerance."""

        lenght = len(old_name)
        if tolerance[0] > lenght:
            return ""
        if tolerance[1] > lenght:
            tolerance[1] = lenght
        return old_name[tolerance[0] - 1:tolerance[1] + 1]

    working_directory = Path.cwd()
    counter = 1
    for obj in working_directory.iterdir():
        if obj.is_dir():
            new_path = working_directory / obj.name
            for file in new_path.iterdir():
                if file.is_file() and file.suffix == extension_old:
                    new_name = new_part(file.name[:-4]) + wanted_name + str(counter).zfill(count_nums) + extension_new
                    counter += 1
                    Path.rename(file, new_path / new_name)


if __name__ == "__main__":
    renaming_files("wood", count_nums=2, extension_old=".mov", extension_new=".vi", tolerance=[2, 5])
