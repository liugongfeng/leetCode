class Solution:

    def lengthOfLongestSubstring(self, s):
        start = -1
        maxi = 0
        d = {}
        for i in range(len(s)):
            if s[i] in d and d[s[i]] > start:
                start = d[s[i]]
                d[s[i]] = i
            else:
                d[s[i]] = i
                if i - start > maxi:
                    maxi = i - start
        return maxi





s = Solution()
res = s.lengthOfLongestSubstring('pwwkew')
print(res)



