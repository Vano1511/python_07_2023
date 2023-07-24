arg1 = 3
arg2 = "three"
arg3 = [3, 6, 1]
arg4 = (4, "one", "two")

def create_dict_of_args(**kwargs):
    exit_dict = {}
    for key, value in kwargs.items():
        try:
            if hash(value):
                exit_dict[value] = key
        except TypeError:
            exit_dict[f"{value}"] = key
    return exit_dict

print(create_dict_of_args(arg1=arg1, arg2=arg2, arg3=arg3, arg4=arg4))
