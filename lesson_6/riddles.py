import json

__all__ = ["riddles"]


def one_riddle(riddle: str, answers: list, attempts: int) -> int:
    """This function recieve a riddle in string type, list of wright answers
    and numbers of attempts. Ask user for answer and return attempt of wright
    attempt or 0 if attempts are out"""

    print(riddle)
    attempt = 1
    while attempt <= attempts:
        answer = input(f"осталось попыток: {attempts - attempt + 1}. ваш ответ->")
        if answer.lower() in answers:
            print(f"вы угадали с {attempt} попытки")
            return attempt
        else:
            print("не угадали")
            attempt += 1
    return 0


def riddles():
    """The function read from json file dictionary with riddles and answers
    and ask of all riddles to user"""

    def results_(riddle: str, attempt: int):
        """The function recieve a riddle and attempt and return result dictionary"""

        global _result_dict
        _result_dict[riddle] = attempt

    with open("riddles.json", encoding="utf-8") as file:
        riddles_dict = json.load(file)
    for key, value in riddles_dict.items():
        *answers, attempts = value
        results_(key, one_riddle(key, answers, attempts))


def show_results(res: iter):
    """This function recieve iterator of results and print results perfectly."""

    for num, pair in enumerate(res, start=1):
        if pair[1] != 0:
            print(f"на {num}-ю загадку вы ответили с {pair[1]}-й попытки")
        else:
            print(f"на {num}-ю загадку вы не ответили правильно")


if __name__ == "__main__":
    _result_dict = {}
    riddles()
    results = ((riddle, result) for riddle, result in _result_dict.items())
    show_results(results)
