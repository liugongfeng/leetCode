class Solution:

    def searchInsert(self, nums, target):
        """
        :param nums: List [int]
        :param target: int
        :return: int
        """
        if target > nums[-1]:
            return len(nums)

        for i in range(len(nums)):
            if nums[i] >= target:
                return i