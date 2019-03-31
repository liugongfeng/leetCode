class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return self.halfIsom(s, t) and self.halfIsom(t, s)


    def halfIsom(self, s, t):
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = t[i]
            elif d[s[i]] != t[i]:
                return False

        return True