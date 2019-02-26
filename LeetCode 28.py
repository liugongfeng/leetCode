class Solution:

    def strStr(self, haystack, needle):
        """
        :param haystack: str
        :param needle: str
        :return: int
        """
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1

        """  trick solution"""

    def strStr2(self, haystack, needle):
        return haystack.find(needle)