from shares import Share
import json
from datetime import datetime
from os.path import join


def take_from_file(name) -> dict:
    """Reads from portfolio file all history"""
    try:
        with open(join("history", f"{name}_portfolio.json"), encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    return data


def current_portfolio(data: dict) -> list:
    """Takes from all history last portfolio and return list."""
    try:
        list_of_shares = data[max(data.keys())]
    except ValueError:
        return []
    res_list = []
    for share_dict, quantity in list_of_shares:
        share = Share(**share_dict)
        res_list.append([share, quantity])
    return res_list


class Portfolio:
    def __init__(self, name):
        self.name = name
        self._list_of_shares = current_portfolio(take_from_file(self.name))

    def add_share(self, full_name, abbreviation, price, quantity):
        share = Share(full_name, abbreviation)
        share.new_current_price(price)
        self._list_of_shares.append([share, quantity])

    def get_value(self):
        """Calculate value of portfolio."""
        port_value = 0
        for share, quantity in self._list_of_shares:
            port_value += share.current_price * quantity
        return port_value

    def write_into_file(self):
        """Serialize portfolio to json file"""
        json_form = []
        for share, quantity in self._list_of_shares:
            json_form.append([{"full_name": share.full_name, "abbreviation": share.abbreviation}, quantity])
        data = take_from_file(self.name)
        data[str(datetime.now())[:16]] = json_form
        with open(join("history", f"{self.name}_portfolio.json"), "w", encoding="utf-8") as file:
            json.dump(data, file, indent=1)

    def calculate_return(self):
        total_return = 0
        for share, quantity in self._list_of_shares:
            total_return += (share.current_price - share.start_price) * quantity
        return total_return

    def most_profitable_stock(self):
        """Returns abbreviation and max profit of profitable stock."""
        max_profit = -10000000
        share_name = None
        for share, quantity in self._list_of_shares[1:]:
            share_profit = (share.current_price - share.start_price) * quantity
            if max_profit < share_profit:
                max_profit = share_profit
                share_name = share.abbreviation
        return share_name, max_profit

    def show_list_of_shares(self):
        for share, quantity in self._list_of_shares:
            print(share.abbreviation, share.current_price, quantity)


if __name__ == "__main__":
    my_portfolio = Portfolio("first")
    # my_portfolio.add_share("Google", "GGL", 410.40, 4)
    # my_portfolio.add_share("Tesla", "TSL", 410.40, 4)
    # my_portfolio.write_into_file()
    print(my_portfolio.most_profitable_stock())
    # my_portfolio.show_list_of_shares()
    print(my_portfolio.calculate_return())
