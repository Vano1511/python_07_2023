import csv
from math import sqrt
from random import randint
from decorators import from_file, json_cashe

coefs_file = "coefficients.csv"
answers_file = "answers.json"


@from_file(coefs_file)
@json_cashe(answers_file)
def find_roots(a=0, b=0, c=0):
    """Finds the roots of the quadratic equation."""
    if a == 0:
        if b == 0:
            return "no roots"
        else:
            return -c / b
    else:
        disc = b * b - 4 * a * c
        if disc < 0:
            return "no roots"
        elif disc == 0:
            return -b / (2 * a)
        else:
            return float((-b - sqrt(disc)) / (2 * a)), float((-b + sqrt(disc)) / (2 * a))


def create_coefs(count: int):
    """Creates count of coefficients a, b, c for quadratic equation and write they to the csv file."""
    with (open(coefs_file, "w", newline="", encoding="utf-8") as file):
        writer = csv.DictWriter(file, fieldnames=["a", "b", "c"])
        writer.writeheader()
        for _ in range(count):
            new_dict = {}
            new_dict["a"] = randint(-20, 20)
            new_dict["b"] = randint(-20, 20)
            new_dict["c"] = randint(-20, 20)
            writer.writerow(new_dict)


if __name__ == "__main__":
    create_coefs(randint(100, 1000))
    find_roots()
