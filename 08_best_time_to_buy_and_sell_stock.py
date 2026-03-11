class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        bestprice = prices[0]
        profit = 0
        for toprice in prices[1: ]:
            if toprice < bestprice:
                bestprice = toprice
            profit = max(profit,toprice - bestprice)
        return profit