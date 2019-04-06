class Solution:
    def addDigits(self, num):
        while num > 9:
            num = sum([int(s) for s in str(num)])
        return num


    def method_2(self, num):
        if num <= 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9