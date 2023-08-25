from random import random, choice, randint

VOWELS = ("a", "e", "u", "i", "o", "y")
ALL_LETTERS = ("q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d",
               "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m")
pairs_file = "pairs.txt"
words_file = "words.txt"
count = 3


def create_pairs(file_path, rows):
    with open(file_path, "a", encoding="utf-8") as file:
        for row in range(rows):
            first = int(random() * 2000 - 1000)
            second = float(random() * 2000 - 1000)
            file.write(f"{first}|{second}\n")


def random_name(min_chr=4, max_chr=7):
    """This function write to file random words of length from 4 to 7."""

    def chair(iterated):
        """Returns random letter"""

        return choice(iterated)

    word = ""
    length = randint(min_chr, max_chr)
    middle = int(length / 2)
    for _ in range(length):
        if _ == middle - 1 or _ == middle + 2:
            word += chair(VOWELS)
        else:
            word += chair(ALL_LETTERS)
    return word.capitalize()


def words_to_file(file_path, counter):
    """Writes words to file """

    with open(file_path, "a", encoding="utf-8") as file:
        for _ in range(counter):
            row = random_name() + "\n"
            file.write(row)


if __name__ == "__main__":
    pass
    # create_pairs(pairs_file, count)
    # words_to_file(words_file, count)
