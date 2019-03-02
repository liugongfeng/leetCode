class Solution:

    def climbStairs(self, n):
        """
        :param n: int
        :return: int
        """
        prev, current = 0, 1
        for i in range(n):
            prev, current = current, prev + current
        return current