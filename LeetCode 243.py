class Solution:
    def shortestDistance(self, words: list[str], word1: str, word2:str) -> int:
        dist = float('inf')
        i, index1, index2 = 0, None, None

        while i < len(words):
            if words[i] == word1:
                index1 = i
            elif words[i] == word2:
                index2 = i
            
            if index1 and index2:
                dist = min(dist, abs(index1 - index2))

        return dist
