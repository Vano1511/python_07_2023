import csv
import json


def from_file(file_name):
    """Decorator who takes keys from csv files and and calls decorating function with this args"""
    with open(file_name, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file, fieldnames=["a", "b", "c"])
        coef_list = []
        for i, line in enumerate(reader):
            if i != 0:
                coef_list.append((map(int, (line["a"], line["b"], line["c"]))))

    def decor(func):

        def wrapper(a=0, b=0, c=0):
            return func(a, b, c)

        for coefs in coef_list:
            wrapper(*coefs)

        return wrapper
    return decor


def json_cashe(file_name):
    """Decorator whom writes to json file args and result of decorating function with args"""
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            res_dict = json.load(file)
    except FileNotFoundError:
        res_dict = {}

    def decor(func):
        def wrapper(a, b, c):
            if a != 0 and b != 0 and c != 0:
                key = f"{a}, {b}, {c}"
                if key in res_dict.keys():
                    return res_dict[key]
                else:
                    val = func(a, b, c)
                    res_dict.update({key: val})
                    with open(file_name, "w", encoding="utf-8") as file:
                        json.dump(res_dict, file, indent=4, sort_keys=True)
                return val


        return wrapper

    return decor
