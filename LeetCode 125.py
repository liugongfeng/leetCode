class Solution:

    def isPalindrome(self, s):
        """
        https://www.youtube.com/watch?v=RYOT5VSLjc4
        :param s:  str
        :return:  bool
        """
        i , j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
