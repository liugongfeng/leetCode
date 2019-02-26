class Solution:

    def permute(self, nums):
        """
        :param nums: List [int]
        :return: List [int]
        """
        if len(nums) <= 1:
            return [nums]

        result = []
        for i, num in enumerate(nums):
            n = nums[:i] + nums[i+1 : ]
            for y in self.permute(n):
                result.append([num] + y)

        return result
