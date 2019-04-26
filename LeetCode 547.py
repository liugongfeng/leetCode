class Solution:
    def findCircleNum(self, M) -> int:
        """ M: list[list[int]]
            rtype: int
        """
        visited = [0] * len(M)
        count = 0
        for i in range(len(M)):
            if visited[i] == 0:
                self.DFS(M, visited, i)
                count += 1
        return count



    def DFS(self, grid, x, y):
        pass

s = Solution()
grid =[ [1,1,0],
        [1,1,0],
        [0,0,1] ]

res = s.findCircleNum(grid)
print(res)
