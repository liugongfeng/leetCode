class Solution:

    def singleNumber(self, nums):
        """
        https://www.youtube.com/watch?v=zAXk82X7hhU
        :param nums: List [int]
        :return:  int
        """
        ans = 0
        for num in nums:
            ans ^= num

        return ans

