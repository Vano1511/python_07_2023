def intersect(entry_dict):
    friends = tuple(entry_dict.keys())
    intersector = set()
    for i in range(len(entry_dict)):
        if i == 1:
            intersector = set(entry_dict[friends[i]]).intersection(set(entry_dict[friends[i - 1]]))
        else:
            intersector = set(entry_dict[friends[i]]).intersection(intersector)
    return intersector


def only_mine(entry_dict):
    friends = tuple(entry_dict.keys())
    friend = input(f"which of friends {friends} will you choose? -> ")
    mine = set(entry_dict[friend])
    for i in range(len(entry_dict)):
        if friends[i] == friend:
            continue
        else:
            mine -= set(entry_dict[friends[i]])
    return friend, mine


def all_except_one(entry_dict):
    friends = tuple(entry_dict.keys())
    dict_len = len(entry_dict)
    result_dict = {}
    for i in range(dict_len):
        new_dict = dict(entry_dict)
        friend = friends[i]
        new_dict.pop(friend)
        result_dict[friend] = intersect(new_dict) - set(entry_dict[friend])
    return result_dict


def add_new_friend(name: str, subjects: tuple, all_friends: dict):
    if name in all_friends.keys():
        print("friend with same name already exists")
    else:
        all_friends[name] = subjects
    return all_friends


start_dict = {
    "Alex": ("book", "guitar", "knife", "magnifying glass", "matches", "mirror",),
    "Mike": ("knife", "milk", "line", "dog", "umbrella", "tent", "matches",),
    "John": ("chess", "bread", "book", "matches", "flower", "fishing rood", "umbrella",),
}

print(all_except_one(start_dict))
print(intersect(start_dict))
print(only_mine(start_dict))
start_dict = add_new_friend(
    "Ilon",
    ("leather", "book", "matches", "corn", "dog", "guitar", "umbrella"),
    start_dict
)
print(intersect(start_dict))
print(only_mine(start_dict))
print(all_except_one(start_dict))
