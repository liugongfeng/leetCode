class Solution:
    """ Example 1:
    Input: 123
    Output: 321

    Example 2:
    Input: -123
    Output: -321

    Example 3:
    Input: 120
    Output: 21
    """

    def reverse(self, x):
        """
        :param x: int
        :return: int
         range: -2^31 ~ 2^31
        """
        num = 0
        a = abs(x)  # return the absolute value of a number
        while a != 0:
            temp = a % 10
            num = num * 10 + temp
            a = a // 10

        if x > 0 and num < 2**31:
            return num
        elif x < 0 and num <= 2**31:
            return -num
        else:
            return 0



