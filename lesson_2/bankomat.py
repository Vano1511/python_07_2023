import constants as con


def withdrawal_fee(amount):
    fee = amount * con.FEE
    if fee < con.MIN_FEE:
        return con.MIN_FEE
    elif fee > con.MAX_FEE:
        return con.MAX_FEE
    else:
        return fee


class Cashomat:
    transaction = 0


    def __init__(self):
        self._account = 0
        self.transaction_list = []

    def show_account(self):
        print(f"остаток на счете : {round(self._account, 2)}")
        self.transaction_list.append(f"остаток : {self._account}")

    def add_funds(self, amount):
        self._account += amount
        self.transaction += 1
        self.transaction_list.append(f"пополнение на {amount}")

    def withdraw_funds(self, summ):
        self.transaction += 1
        summ_with_fee = summ + withdrawal_fee(summ)
        if self._account < summ_with_fee:
            print("неверная операция : сумма для снятия больше, чем остаток на счете")
            self.transaction_list.append(f"неверная операция")
        else:
            print(f"возьмите {summ} наличных")
            self._account -= summ_with_fee
            self.transaction_list.append(f"выдача {summ} наличных")


    def check_for_procent(self):
        if self.transaction % con.TRANSACTION_FOR_PROC == 0:
            self._account = round(self._account * (1 + con.PROC), 2)
            print("проценты на остаток начислены")
            self.transaction_list.append(f"проценты на остаток начислены")

    def check_for_richy(self):
        if self._account > con.RICHY_SUM:
            tax = self._account * con.RICHY_TAX
            self._account -= tax
            print(f"произведен вычет налога на богатство в размере {tax}")
            self.transaction_list.append(f"вычет налога на богатство в размере {tax}")

    def show_history(self):
        print("история счета: ")
        for num, element in enumerate(self.transaction_list, start=1):
            print(f"{num} : {element}")


# if __name__ == "__main__":
    # new = Cashomat()
    # new.add_funds(15000)
    # new.check_for_procent()
    # new.withdraw_funds(10000)
    # print(new.show_account())
