class Solution:

    def maxProfit(self, prices):
        """
        :param prices: List[int]
        :return:   int
        """
        if len(prices) < 2:
            return 0

        total = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                total += prices[i] - prices[i - 1]

        return total
