class Solution:
    def trailingZeros(self, n):
        result = 0

        while n:
            result += n // 5
            n = n // 5
        return result


    def method2(self, n):
        return 0 if n == 0 else n // 5 + self.method2(n // 5)