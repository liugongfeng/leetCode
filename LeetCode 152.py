class Solution:
    def maxProduct(self, nums):
        res = big = small = nums[0]

        for n in nums[1:]:
            big, small = max(n, n*big, n*small), min(n, n*big, n*small)
            res = max(big, res)

        return res