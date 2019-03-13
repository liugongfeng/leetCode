class Solution:
    def isPowerOfTwo(self, n):
        if n == 1:
            return True
        while n:
            if n == 1:
                return True
            elif n % 2 == 0:
                n = n // 2
            else:
                return False

