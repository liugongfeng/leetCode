class Solution:
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        result = 0

        while left < right:
            water = min(height[left], height[right]) * (right - left)
            if water > result:
                result = water
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return result