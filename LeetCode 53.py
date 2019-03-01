class Solution:

    def maxSubArray(self, nums):
        """
        :param nums: List[int]
        :return: int
        """
        if max(nums) < 0:
            return max(nums)

        local_max , global_max = 0, 0
        for num in nums:
            local_max = max(0, local_max + num)
            global_max = max(global_max, local_max)

        return global_max

    """ [-2, 1, -3, 4, -1, 2, 1, -5, 4]"""

if __name__ == "__main__":
    s = Solution()
    result = s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print(result)