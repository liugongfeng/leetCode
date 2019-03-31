class Solution:
    def longestPalindrome(self, s):
        palindrome = ""

        for i in range(len(s)):
            strs1 = self.getLongestPalindrome(s, i, i)
            if len(strs1) > len(palindrome):
                palindrome = strs1

            strs2 = self.getLongestPalindrome(s, i, i+1)
            if len(strs2) > len(palindrome):
                palindrome = strs2

        return palindrome


    def getLongestPalindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

