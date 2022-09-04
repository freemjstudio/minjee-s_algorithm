class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        result = 0

        min_price = prices[0]
        for price in prices[1:]:
            if price < min_price:
                min_price = price
            elif result < price - min_price:
                result = price - min_price
        return result