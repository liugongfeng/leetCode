class Solution:
    def rob(self, nums):
        last, now = 0, 0
        for num in nums:
            last, now = now, max(last + num, now)
        
        return now

s = Solution()
res = s.rob([2,7,9,3,1])
print(res)