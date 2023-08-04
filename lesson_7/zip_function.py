from randoms import pairs_file, words_file
newest_file = "pairs_mult.txt"


def mult_numbers(pair_of_numbers: str) -> float:
    """Recieve a string with number splited '|' and returns its multiplying"""

    # parse string to two numbers
    first, second = list(map(lambda string: float(string.replace("\n", "")), pair_of_numbers.split("|")))
    return first * second


def pairs_to_new_file(pair_file, name_file, new_file):
    """reads files and writes to new file pairs of name and multiplying of pairs of numbers."""

    def write_to_file(file_name, large_list, small_list):
        """Writes to file"""

        loop = len(small_list)
        multiplier = 0
        with open(file_name, "w", encoding="utf_8") as file:
            for operation, element in enumerate(large_list, start=1):
                if operation % loop == 0:
                    multiplier += 1
                # check for number
                if filter(str.isdigit, element):
                    mult = mult_numbers(element)
                    name = small_list[operation - 1 - multiplier * loop]
                else:
                    name = mult_numbers(element)
                    mult = small_list[operation - 1 - multiplier * loop]
                if mult > 0:
                    row = f"{name[:-1].upper()} : {int(mult)}\n"
                else:
                    row = f"{name[:-1].lower()} : {abs(mult)}\n"
                file.write(row)

    with (
            open(pair_file, "r", encoding="utf-8") as file1,
            open(name_file, "r", encoding="utf-8") as file2
    ):
        names_list = file2.readlines()
        pairs_list = file1.readlines()
    if len(names_list) >= len(pairs_list):
        write_to_file(new_file, names_list, pairs_list)
    else:
        write_to_file(new_file, pairs_list, names_list)


pairs_to_new_file(pair_file=pairs_file, name_file=words_file, new_file=newest_file)
