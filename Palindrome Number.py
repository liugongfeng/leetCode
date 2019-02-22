class Solution:

    def isPalindrome(self, x):
        num = 0
        a = abs(x)

        while a != 0:
            temp = a % 10
            num = num * 10 + temp
            a = a // 10

        if x >= 0 and x == num:
            return True
        else:
            return False

    """ Anothe Solution. """
    def isPalin(self, x):
        if x > 0:
            return str(x) == str(x)[::-1]
        else:
            return False

