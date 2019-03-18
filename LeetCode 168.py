class Solution:
    def convertToTitle(self, n):
        result , num = "", n

        while num:
            result += chr( (num - 1) % 26 + ord('A') )
            num = (num - 1) // 26

        return result[::-1]



s = Solution()
rest = s.convertToTitle(702)
print(rest)