class Solution:
    def containsDuplicate(self, nums):
        res = set()
        for e in nums:
            if e not in res:
                res.add(e)
            else:
                return True
        return False