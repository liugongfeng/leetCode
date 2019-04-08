class Solution:
    def titleToNumber(self, s):
        result = 0
        for i, v in enumerate(s):
            result *= 26
            result += ord(v) - ord('A') + 1
        return result