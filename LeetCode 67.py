class Solution:

    def addBinary(self, a, b):
        """
        :param a: str
        :param b: str
        :return: str
        """
        result , carry, val = "", 0, 0
        for i in range(max(len(a), len(b))):
            val = carry
            if i < len(a):
                val += int(a[-(i+1)])
            if i < len(b):
                val += int(b[-(i+1)])

            carry, val = val // 2, val % 2
            result += str(val)

        if carry:
            result += str(1)
        return result[::-1]


if __name__ == "__main__":
    s = Solution()
    result = s.addBinary("1010", "1011")
    print(result)

