class Solution:
    def moveZeroes(self, nums: 'List[int]') -> None:
        pos = 0
        for i, v in enumerate(nums):
            if v:
                nums[pos] = v
                pos += 1
        
        for i in range(pos, len(nums)):
            nums[i] = 0

            
        # method 2:
        # nums.sort(key=bool, reverse=True)


        # method 3:
        # zeros = nums.count(0)
        # for _ in range(zeros):
        #     nums.remove(0)
        # nums.extend([0] * zeros)