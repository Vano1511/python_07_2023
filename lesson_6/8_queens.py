from random import randint


def check_solve(places: list) -> bool:
    """This function check a placement of 8 queens and returns bool result of solving task"""

    end = len(places)
    for f_num, first in enumerate(places, start=1):
        for second in places[f_num: end + 1]:
            one = abs(first[0] - second[0])
            two = abs(first[1] - second[1])
            if first[0] == second[0] or first[1] == second[1] or one == two:
                return False
    return True


def placements_gen():
    """This function generate random placement of 8 queens and returns list of tuples"""

    result = []
    while len(result) < 8:
        queen = (randint(1, 8), randint(1, 8))
        if queen in result:
            continue
        else:
            result.append(queen)
    return result


if __name__ == "__main__":
    # count = 0
    # while count < 4:
    #     placement = placements_gen()
    #     if check_solve(placement):
    #         print(placement)
    #         count += 1
    print(placements_gen())
