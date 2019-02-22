class Solution:

    def longestCommonPrefix(self, strs):
        """
        :param strs: List[str]
        :return:    str
        """
        if not strs or len(strs)==0:
            return ""

        """
        Input: ["flower","flow","flight"]
        Output: "fl"
        """
        for i in range(len(strs[0])):
            for string in strs[1:]:
                if i >= len(string) or string[i] != strs[0][i]:
                    return strs[0][:i]


