class Solution:

     def romanToInteger(self, s):
         """
         :param s: str
         :return: int
         """
         d = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
         result = 0
         for i in range(len(s)):
             if i > 0 and d[s[i]] > d[s[i-1]]:
                 result += d[s[i]] - 2 * d[s[i-1]]
             else:
                 result += d[s[i]]

         return result

