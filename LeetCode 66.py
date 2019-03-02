class Solution:

    def plusOne(self, digits):
        """
        :param digits: List [int]
        :return: List [int]
        """
        for i in range(len(digits) - 1, 0, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits

        digits[0] = 1
        digits.append(0)

        return digits