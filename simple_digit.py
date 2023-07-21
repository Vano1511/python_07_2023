while True:
    try:
        number = int(input("Введите целое число (от 0 до 100_000) и я проверю, является ли оно простым > "))
        if number < 0 or number > 100_000:
            print("нельзя вводить отрицательное число и число больше 100 тыс.")
            continue
        break
    except:
        print("вы ввели не число, попробуйте еще раз")

simple = True
for _ in range(2, number // 2 + 1):
    if number % _ == 0:
        print("число не простое ) ")
        simple = False
        break

if simple:
    print("вы ввели простое число")
