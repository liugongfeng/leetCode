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


    def DFS(self, M, visited, i):
        for j in range(len(M)):
            if M[i][j] == 1 and visited[j] == 0:
                visited[j] = 1
                self.DFS(M, visited, j)


    """ Solution 2"""
    def findCircleNum2(self, M):
        def find(node):
            if circles[node] == node:
                return node
            root = find(circles[node])
            circles[node] = root
            return root

        n = len(M)
        circles = {x: x for x in range(n)}
        
        for i in range(n):
            for j in range(i, n):
                if i != j and M[i][j]==1 and find(i) != find(j):
                    circles[find(i)] = find(j)
                    
        return sum([1 for k,v in circles.items() if k==v])


s = Solution()
grid =[ [1,1,0],
        [1,1,0],
        [0,0,1] ]

res = s.findCircleNum2(grid)
print(res)
