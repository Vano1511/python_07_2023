from calendar import isleap
from datetime import date

__all__ = ["check_date"]
MIN_DATE = date(1, 1, 1)
MAX_DATE = date(2025, 12, 31)


def check_date(dat: date) -> bool:
    if MIN_DATE <= dat <= MAX_DATE:
        return True
    else:
        return False


if __name__ == "__main__":
    _leap_check = lambda x: True if isleap(x.year) else False
    while True:
        input_date = input("Введите дату формата ДД.ММ.ГГГГ и я проверю ее на существование и високосность")
        day, month, year = map(int, input_date.split("."))
        try:
            my_date = date(year, month, day)
            break
        except ValueError:
            print("неправильная дата")
    print("дата существует" if check_date(my_date) else "дата не существует")
    print("год високосный" if _leap_check(my_date) else "год невисокосный")
