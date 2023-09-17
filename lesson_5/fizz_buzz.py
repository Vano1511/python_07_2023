def fizz_gen():
    for i in range(1, 101):
        if i % 3 == i % 5 == 0:
            i = "FizzBuzz"
        elif i % 3 == 0:
            i = "Fizz"
        elif i % 5 == 0:
            i = "Buzz"
        yield i


if __name__ == "__main__":
    for num, element in enumerate(fizz_gen(), start=1):
        print(f"{num} : {element}")