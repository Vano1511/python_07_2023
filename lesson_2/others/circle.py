from math import pi
import decimal as dec


def circle_square(radius):
    return pi * (radius / 2) ** 2


def circle_long(radius):
    return 2 * pi * radius


def check_input():
    loop_message = "введите диаметр окружности (от 0 до 1000) -> "
    enter = None
    while not enter:
        try:
            enter = float(input(loop_message))
        except ValueError:
            print("я вас не понял")
        if 0 >= enter <= 1000:
            print("диаметр выходит из допустимого диапазона")
            enter = None
    return enter


if __name__ == "__main__":
    entry_message = "Здравствуйте, введите диаметр окружности и я посчитаю вам ее площадь и длину"
    print(entry_message)
    dec.getcontext().prec = 42
    user_radius = check_input() / 2
    print(f"площадь круга радиусом {user_radius} равна {dec.Decimal(circle_square(user_radius))}")
    print(f"длина окружности радиусом {user_radius} равна {dec.Decimal(circle_long(user_radius))}")
