def making_list_of_columns(columns_count: int):
    counter = 0
    row_list =[]
    exit_list = []
    for digit in range(2, 10):
        counter += 1
        row_list.append(digit)
        if counter == columns_count:
            counter = 0
            exit_list.append(tuple(row_list))
            row_list.clear()
    exit_list.append(tuple(row_list))
    return exit_list

MAX_LENGTH = 15

count_of_columns = int(input("В скольких столбцах вам вывести таблицу умножения (максимально 8): ")) # тут без проверки на дурака
columns_list = making_list_of_columns(count_of_columns)

print("-" * 15 + "ТАБЛИЦА УМНОЖЕННИЯ" + "-" * 15, end="\n\n")
for columns in columns_list:
    for digit in range(2, 10):
        for column in columns:
            row = f"{column}*{digit} = {column * digit}"
            print(row + " " * (MAX_LENGTH - len(row)), end="")
        print()
    print()
