def fib(n: int) -> int:
    a = 1
    b = 1
    for _ in range(n - 1):
        a, b = b, a+b
        yield a


answer = int(input("введите, какое по счету число Фиббоначи вым выдать -> "))
my_answer = None
for element in fib(answer):
    my_answer = element
print(my_answer)
