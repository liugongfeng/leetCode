class Solution:

    def lenLongestFibSubSeq(self, A):
        """
        :param A: List[int]
        :return: int
        """
        s = set(A)
        n = len(A)
        result = 0

        for i in range(n-1):
            for j in range(i + 1, n):
                a, b = A[i], A[j]
                count = 2
                while a + b in s:
                    a, b = b, a + b
                    count += 1
                    result = max(result, count)

        if result > 2:
            return result
        else:
            return 0
