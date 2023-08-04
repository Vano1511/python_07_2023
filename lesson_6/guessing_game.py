from random import randint

START = 0
FINISH = 100
ATTEMPTS = 5
__all__ = ["guess_body"]


def checking_answer(one, two, three: str) -> tuple:
    one = int(one) if one != "" else START
    two = int(two) if two != "" else FINISH
    three = int(three) if three != "" else ATTEMPTS
    return one, two, three


def guess_body(start, finish, attemps) -> bool:
    wright_answer = randint(start, finish)
    attempt = 1
    print(f"Приветствую, я загадал число {start} от до {finish}, чтобы угадать его у вас есть\n"
          f"попыток: {attemps},\n"
          f"я буду давать подсказки 'больше' или 'меньше', погнали!")
    while attempt <= attemps:
        user_answer = int(input(f"попытка {attempt}, осталось попыток: {attemps - attempt} -> "))
        if user_answer == wright_answer:
            print(f"поздравляю, вы угадали, я загадал число {wright_answer}! ")
            return True
        elif user_answer > wright_answer:
            print(f"мое число МЕНЬШЕ вашего")
        else:
            print(f"мое число БОЛЬШЕ вашего")
        attempt += 1
    print(f"ваши попытки закончились, я загадал число {wright_answer}")
    return False


if __name__ == "__main__":
    welcome_message = "Приветсвую, поиграем в угадайку, по умолчанию я задумываю число в интервале\n" \
                      "от 0 до 100 и у вас есть 5 попыток, чтобы угадать его\n" \
                      "я спрошу у вас три этих показателя, если не хотите менять, то просто нажмите ENTER"
    print(welcome_message)
    start_ = input(f"введите нижнюю границу диапазона->")
    finish_ = input(f"введите верхнюю границу диапазона->")
    attempts_ = input(f"введите количество желаемых попыток->")
    print(guess_body(*checking_answer(start_, finish_, attempts_)))
