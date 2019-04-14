from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums):
        num = list(map(str, nums))
        num.sort(key = cmp_to_key(lambda b, a: ((a+b)<(b+a))-((a+b)>(b+a)) ))
        return ''.join(num).lstrip('0') or '0'

    
    def method2(self, nums):
        def cmp(a, b):
            return int(b+a) - int(a+b)
        
        nums = list(map(str, nums))
        nums.sort(key=cmp_to_key(cmp))
        return ''.join(nums).lstrip('0') or '0'
        
