from collections import defaultdict

class Solution:
    def intersect(self, nums1, nums2):
        d = defaultdict(int)
        result = []
        
        for i in nums1:
            d[i] += 1
        
        for j in nums2:
            if d[j]>0:
                result.append(j)
                d[j] -= 1
                
        return result
       

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
s =Solution()
res = s.intersect(nums1, nums2)