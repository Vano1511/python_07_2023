import fractions as fr
from math import lcm, gcd


def simple_frac(frac_list):
    frac_list = list(frac_list)
    delimiter = 0
    while delimiter != 1:
        delimiter = gcd(int(frac_list[0]), int(frac_list[1]))
        frac_list[0] /= delimiter
        frac_list[1] /= delimiter
    return int(frac_list[0]), int(frac_list[1])


def summ_frac(one, two):
    down = lcm(one[1], two[1])
    up = int(one[0] * down / one[1] + two[0] * down / two[1])
    return up, down


def mult_frac(one, two):
    up = one[0] * two[0]
    down = one[1] * two[1]
    return up, down


first = list(map(int, input("введите первую дробь -> ").split("/")))
second = list(map(int, input("введите вторую дробь -> ").split("/")))
first_frac = fr.Fraction(int(first[0]), int(first[1]))
second_frac = fr.Fraction(int(second[0]), int(second[1]))
frac_sum = simple_frac(summ_frac(first, second))
frac_mult = simple_frac(mult_frac(first, second))
print(f"сумма дробей равна : {frac_sum[0]}/{frac_sum[1]}")
print(f"проверка {first_frac + second_frac}")
print(f"произведение дробей равно : {frac_mult[0]}/{frac_mult[1]}")
print(f"проверка {first_frac * second_frac}")
