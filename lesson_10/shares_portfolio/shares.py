import json
from datetime import datetime
from os.path import join
import pandas as pd
import matplotlib.pyplot as plt


def take_price_history(share_name):
    try:
        with open(join("history", f"{share_name}.json"), encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    return data


class Share:

    def __init__(self,
                 full_name: str,
                 abbreviation: str):
        self.full_name = full_name
        self.abbreviation = abbreviation.upper()
        self._price_history = take_price_history(self.abbreviation)
        try:
            self.current_price = self._price_history[max(self._price_history.keys())]
            self.start_price = self._price_history[min(self._price_history.keys())]
        except ValueError:
            self.current_price = None
            self.start_price = None

    def new_current_price(self, price: float):
        """Rewrites current_price attribute and rewrites file with price history."""
        self._price_history[str(datetime.now())[:16]] = price
        self.current_price = price
        if not self.start_price:
            self.start_price = price
        with open(join("history", f"{self.abbreviation}.json"), "w", encoding="utf-8") as file:
            json.dump(self._price_history, file, indent=1)

    def show_price_history(self):
        data = pd.DataFrame.from_dict(self._price_history, orient="index")
        plt.plot(data)
        plt.ylabel("Dollars")
        plt.xlabel("Date")
        plt.xticks(size=10, rotation=20)
        plt.title(self.full_name)
        plt.show()


if __name__ == "__main__":
    google = Share("GOOGLE", "GGL")
    # google.new_current_price(398.89)
    print(google.current_price)
    print(google.start_price)

    # google.show_price_history()
