class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        d1 , d2 = {}, {}
        for item in s:
            d1[item] = d1.get(item, 0) + 1
        for item in t:
            d2[item] = d2.get(item, 0) + 1
        return d1 == d2


    def isAnagram_2(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
