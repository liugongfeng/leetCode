class Solution:
    def letterCombinations(self, digits):
        if len(digits) == 0:    return []

        d = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno','7':'pqrs', '8':'tuv', '9':'wxyz'}

        result = ['']
        for e in digits:
            temp = []
            for ch in d[e]:
                for res in result:
                    temp.append(res + ch)
            result = temp
        return result