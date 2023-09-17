import json


def check_id(users_dict: dict, new_id: str) -> bool:
    """Checks new user's id for unique value and returns True if id is unique."""

    is_uniqe = True
    for user in users_dict.values():
        if new_id in user.keys():
            is_uniqe = False
    return is_uniqe


def enter_new_user() -> tuple:
    """Asks for data of new user(id, name, access_level) and returns tuple of user's data."""
    print("Please enter new user data for QUIT enter 'q'")
    user_id = input("enter unique id of new user: ")
    name = input("name of new user: ")
    level = input("enter access level of new user: ")
    return user_id, name, level


def read_from_file(file_name: str) -> dict:
    """Opens json file to read data and returns data of users."""

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {f"access_level_{i}": {} for i in range(1, 8)}
    return data


def write_to_file(file_name: str, user_id: str, user_name: str, user_access: str, data: dict):
    """Opens json file to write to file."""

    data[f"access_level_{user_access}"].update({user_id: user_name})
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=3)
        print("new user is added\n")



if __name__ == "__main__":
    filename = "users.json"
    while True:
        user_id, user_name, user_level = enter_new_user()
        if "q" in (user_id, user_name, user_level):
            break
        data = read_from_file(filename)
        if check_id(data, user_id):
            write_to_file(filename, user_id, user_name, user_level, data)
        else:
            print(f"\nuser with id {user_id} already exists ")
    print("\nHave a good day!")