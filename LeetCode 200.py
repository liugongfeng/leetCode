class Solution:
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
        
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid or not grid[0]: 
            return 0
        self.max_x = len(grid)
        self.max_y = len(grid[0])
        self.grid = grid
        self.visited = set()
        
        return sum([self.floodfill_DFS(i, j) for i in range(self.max_x) 
                                             for j in range(self.max_y)])


    def floodfill_DFS(self, x, y):
        if not self._is_valid(x, y):
            return 0
        self.visited.add((x, y))
        for k in range(4):
            self.floodfill_DFS(x + self.dx[k], y + self.dy[k])
        return 1


    def _is_valid(self, x, y):
        if x < 0 or x >= self.max_x or y < 0 or y >= self.max_y:
            return False
        if self.grid[x][y] == '0' or ((x,y) in self.visited):
            return False
        return True



    """Solution 2"""
    def numIslands2(self, grid):
        if not grid:
            return 0
        count = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1':
                    self.DFS(grid, x, y)
                    count += 1
        return count

    def DFS(self, grid, x, y):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != '1':
            return 
        grid[x][y] = "#"
        self.DFS(grid, x+1, y)
        self.DFS(grid, x-1, y)
        self.DFS(grid, x, y+1)
        self.DFS(grid, x, y-1)