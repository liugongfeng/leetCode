class Solution:
    def isValid(self, s):
        """
        :param s: str
        :return: bool
        """
        stack = []
        d = {"(": ")", "{": "}", "[": "]" }
        for parenthese in s:
            if parenthese in d:
                stack.append(parenthese)
            elif len(stack) == 0 or d[stack.pop()] != parenthese:
                return False
        return len(stack) == 0

        """ { [ ] } 
            [ { ] }
        """
