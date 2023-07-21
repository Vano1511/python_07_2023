levels = int(input("введите количество уровней елочки: "))
size = levels * 2 - 1
for level in range(1, levels + 1):
    stars = level * 2 - 1
    spaces = int((size - stars) / 2)
    print(" " * spaces, "*" * stars, " " * spaces, sep="")
