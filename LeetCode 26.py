class Solution:

    def removeDuplicates(self, nums):
        """
        :param nums: List[int]
        :return: int
        """
        if not nums:
            return 0

        """ [0,0,1,1,1,2,2,3,4] """
        count = 0
        for i in range(len(nums)):
            if nums[count] != nums[i]:
                count += 1
                nums[count] = nums[i]
        return count + 1
