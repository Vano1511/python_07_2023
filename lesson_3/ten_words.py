import re


with open("berlin.txt", encoding="utf-8") as file:
    text = file.read()

# считаем слова
text_list = re.findall("\w+", text)
count_dict = {}
for element in text_list:
    if len(element) > 2:  # отсеиваем маленькие союзы и т.д.
        val = count_dict.get(element.lower(), 0)
        count_dict[element.lower()] = val + 1

#  оставим словарь только из топ слов
sort_values = sorted(count_dict.values(), reverse=True)[:10]
result_dict = {}
for key, value in count_dict.items():
    if value in sort_values:
        result_dict[key] = value

# выведем
print("ТОП 10 слов в статье: ")
for i in range(1, 11):
    for key, value in result_dict.items():
        if value == sort_values[i - 1]:
            word = key
    result_dict.pop(word)
    print(f"{i} место слово: {word}, встречалось раз - {sort_values[i - 1]}")
