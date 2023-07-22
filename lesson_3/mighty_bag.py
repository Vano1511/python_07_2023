from itertools import permutations

subjects = {
    "water": 2,
    "tent": 12,
    "book": 1,
    "bidon": 6,
    "food": 7,
    "laptop": 8,
    "fishing rood": 9,
    "spoon": 5,
}

max_capacity = int(input("enter max capacity of bag (positive integer): "))
print(f"max capacity of the bag is {max_capacity}")
new_set = permutations(subjects)
exit_lists = []
for tup in new_set:
    capasity = max_capacity
    result_list = []
    for subject in tup:
        item_capacity = subjects[subject]
        if capasity >= item_capacity:
            result_list.append(subject)
            capasity -= item_capacity
    result_set = set(result_list)
# для того, чтобы не выводить все перестановки, выведу те, при которых не осталось пустого места
    if capasity == 0 and result_set not in exit_lists:
        print(f"{result_set}, free space - {capasity}")
        exit_lists.append(result_set)
