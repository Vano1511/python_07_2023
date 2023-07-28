MAX_LENGTH = 15
first_row = (f"{j} * {i} = {i * j}" for i in range(2, 10) for j in range(2, 6))
second_row = (f"{j} * {i} = {i * j}" for i in range(2, 10) for j in range(6, 10))
counter = 1
print("-" * 18 + "ТАБЛИЦА УМНОЖЕННИЯ" + "-" * 18, end="\n\n")
for example in (*first_row, *second_row):
    print(f"{example:<{MAX_LENGTH}}", end="")
    if counter % 4 == 0:
        if counter % 32 == 0:
            print()
        print()
    counter += 1
