from bankomat import Cashomat
from constants import MESSAGE, ANSWER_LIST


def input_summ():
    while True:
        try:
            summ = float(input("введите сумму транзакции (кратно 50): -> "))
            if summ % 50 == 0:
                break
        except ValueError:
            print("неверный ввод")
    return summ


def input_operation():
    while True:
        answer = input(MESSAGE)
        if answer in ANSWER_LIST:
            break
        else:
            print("неверный ввод")
    return answer


new_bankomat = Cashomat()
print("Здравствуйте, я ваш виртуальный банкомат!")
exiting = False
while not exiting:
    new_bankomat.show_account()
    user_answer = input_operation()
    if user_answer == "0":
        print("до свидания")
        exit()
    elif user_answer == "3":
        new_bankomat.show_history()
    else:
        new_bankomat.check_for_richy()
        user_sum = input_summ()
        if user_answer == "1":
            new_bankomat.withdraw_funds(user_sum)
        else:
            new_bankomat.add_funds(user_sum)
    new_bankomat.check_for_procent()
