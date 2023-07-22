start_list = [1, 4, 5, 2, 67, 3, 4, 2, 67, 23, 11, 34, 54, 34]
result_dict = {}
for element in start_list:
    value = result_dict.get(element, 0)
    value += 1
    result_dict[element] = value
result_list = []
for key, value in result_dict.items():
    if value > 1:
        result_list.append(key)
print(f"answer: {result_list}")