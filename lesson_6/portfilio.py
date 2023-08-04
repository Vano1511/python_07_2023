share_quantities = {"AAPL": 5, "GOOGL": 6, "MSFT": 8}
_share_start_prices = {"AAPL": 600.5, "GOOGL": 1845, "MSFT": 756.3}
share_next_prices = {"AAPL": 681.1, "GOOGL": 2763.9, "MSFT": 797.1}


def calculate_portfolio_value(stocks: dict, prices: dict) -> float:
    """This function parse dicts with quantities and prices of shares and returns cost of portfolio"""

    cost_of_portfolio = 0
    for share in stocks.keys():
        cost_of_portfolio += stocks[share] * prices[share]
    return cost_of_portfolio


def calculate_portfolio_return(initial_value: float, current_value: float) -> float:
    """This function take start and last portfolio value and returns portfolio profit."""

    return current_value / initial_value - 1


def get_most_profitable_stock(stocks: dict, prices: dict) -> str:
    """This function get a most profitable share in portfolio."""

    global _share_start_prices
    shares = list(_share_start_prices.keys())
    profitable_share = shares[0]
    max_profit = (prices[profitable_share] - _share_start_prices[profitable_share]) * stocks[profitable_share]
    for share in shares[1:]:
        share_profit = (prices[share] - _share_start_prices[share]) * stocks[share]
        if share_profit > max_profit:
            max_profit = share_profit
            profitable_share = share
    return profitable_share


   # for share in _share_start_prices.keys():



if __name__ == "__main__":
    print(get_most_profitable_stock(share_quantities, share_next_prices))
    start = calculate_portfolio_value(share_quantities, _share_start_prices)
    finish = calculate_portfolio_value(share_quantities, share_next_prices)
    print(f"{round(calculate_portfolio_return(start, finish) * 100, 2)}%")
    print(start, finish)

