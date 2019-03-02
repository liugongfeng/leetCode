class Solution:

    def reverseWords(self, s):
        """
        :param s: str
        :return: str
        """
        if s == "" or s.split() == []:
            return ""

        ls = s.split()
        result = ""
        for i in range(0, len(ls) - 1):
            result += ls[len(ls)-1-i] + " "
        result += ls[0]

        return result


    def reverseWords_2(self, s):
        s = s.split()
        s.reverse()
        return ' '.join(s)
