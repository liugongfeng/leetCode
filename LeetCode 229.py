class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        if not nums:
            return []
        d = {}
        result = set()
        for e in nums:
            if e not in d:
                d[e] = 1
            else:
                d[e] += 1
            if d[e] > len(nums) / 3:
                result.add(e)

        return list(result)