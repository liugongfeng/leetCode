class Solution:

    def mojorityElement(self, nums):
        d = {}
        result = set()
        for e in nums:
            if e not in d:
                d[e] = d.get(e, 0) + 1
            else:
                d[e] += 1
            if d[e] > len(nums) / 3:
                result.add(e)
        return result

s = Solution()
result = s.mojorityElement([3,2,3])
print(result)
