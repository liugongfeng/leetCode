class Solution:

    def removeElement(self, nums, val):
        """
        :param nums: List[int]
        :param val: int
        :return: int
        """

        i, last = 0, len(nums) - 1

        while i <= last:
            if nums[i] == val:
                nums[i], nums[last] = nums[last], nums[i]
                last -= 1
            else:
                i += 1

        return last + 1




