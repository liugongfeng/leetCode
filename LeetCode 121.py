class Solution:

    def maxProfit(self, prices):
        """
        https://www.youtube.com/watch?v=TgnftvU8rxc
        :param prices: List[int]
        :return:  int
        """
        profit , min_price = 0, float('inf')

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        return profit
