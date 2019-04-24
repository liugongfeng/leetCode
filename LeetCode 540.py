class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if mid % 2 == 0:
                mid += 1
            if nums[mid] == nums[mid-1]:
                left = mid + 1
            else:
                right = mid - 1
                
        return nums[left]