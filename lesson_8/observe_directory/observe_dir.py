import csv
import json
import os
import pickle

dir_path = os.path.abspath("F:\\учеба\\python_07_2023\\lesson_6")
reports_dir = "reports"
report_name = f"{os.path.basename(dir_path)}_report"
base_dir = dir_path.split("\\")[-1]


def take_file_size(path_dir, files) -> int:
    """Walks on directory and retuns dictionary with keys(filenames) and values(file size)."""

    res_dict: dict = {}
    for file in files:
        file_path = os.path.join(path_dir, file)
        *_, parent_dir, file_name = file_path.split("\\")
        res_dict[file_name] = os.path.getsize(file_path)
    return sum(res_dict.values())


def make_dict_for_raport(path: str):
    """Walks in directory and raporting info on list of dicts"""

    result_list: list = []
    for dirs in os.walk(path):
        obj_path = dirs[0]
        *_, dir_name, file = obj_path.split("\\")
        result_list.append({
            "name": file,
            "parent": dir_name,
            "type": "directory",
            "size": take_file_size(obj_path, dirs[2])
        })
        for file in dirs[2]:
            result_list.append({
                "name": file,
                "parent": dir_name,
                "type": "file",
                "size": os.path.getsize(os.path.join(obj_path, file))
            })
    return result_list


def reporting(data: list):
    """write reports in reports directory."""

    with (
        open(os.path.join(reports_dir, report_name + ".json"), "w", encoding="utf-8") as json_file,
        open(os.path.join(reports_dir, report_name + ".csv"), "w", encoding="utf-8") as csv_file,
        open(os.path.join(reports_dir, report_name + ".pickle"), "wb") as pickle_file,
    ):
        csv_write = csv.DictWriter(csv_file, fieldnames=data[0].keys())
        csv_write.writeheader()
        for el in data:
            csv_write.writerow(el)
        json.dump(data, json_file, indent=4)
        pickle.dump(data, pickle_file)


if __name__ == "__main__":
    report_list = make_dict_for_raport(dir_path)
    reporting(report_list)

    #
    #         if dirs[1]:
    #             for dir in dirs[1]:
    #                 print(f"{file} = {os.path.getsize(os.path.join(dir_path, dir, file))}")
