class Solution:
    def isStrobogrammatic(self, num):
        d = {'0':'0', '1':'1', '6':'9','8':'8','9':'6'}
        n = len(num)

        for i in range((n + 1) // 2):
            if num[n-1-i] not in d or num[i] != d[num[n-1-i]]:
                return False
        return True