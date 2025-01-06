"""121. Best Time to Buy and Sell Stock. """

from typing import List


class StockBuySell:
    def maxProfit(self, prices: List[int]) -> int:
        largest_profit_seen = 0
        lowest_value_seen = 100000  # From constraints (10^5)

        for idx in range(len(prices)):
            if prices[idx] < lowest_value_seen:
                lowest_value_seen = prices[idx]
            else:
                temp_profit = prices[idx] - lowest_value_seen
                if temp_profit > largest_profit_seen:
                    largest_profit_seen = temp_profit

        return largest_profit_seen
