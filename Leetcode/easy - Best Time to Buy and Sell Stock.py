
class Solution:

    def max_profit(self, prices: List[int]) -> int:

        if not prices:
            return 0

        min_price = prices[0]                            # set the first price as a buy price
        max_profit = 0

        for current_price in range(1, len(prices)):      # skip the first price, since we did not buy anything yet
            profit = prices[current_price] - min_price   # profit = current price - buy price

            if profit > max_profit:                      # set current profit as a maximum, if current > than maximum
                max_profit = profit

            if prices[current_price] < min_price:        # set current price as a buy price, if it is smaller than the previous buy price
                min_price = prices[current_price]

        return max_profit


"""
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.
"""