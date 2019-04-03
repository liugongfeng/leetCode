class Solution:
    def totalNQueens(self, n):
        if not n:
            return 0
        
        # self.result = []
        self.result = 0
        self.cols = set();  self.pie = set(); self.na = set()
        self.DFS(n, 0, [])
        return self.result

    def DFS(self, n, row, cur_state):
        if row >= n:
            self.result += 1
            return 

        for col in range(n):
            if col in self.cols or row + col in self.pie or row - col in self.na:
                continue

            self.cols.add(col)
            self.pie.add(row + col)
            self.na.add(row - col)

            self.DFS(n, row + 1, cur_state + [col])
            
            self.cols.remove(col)
            self.pie.remove(row + col)
            self.na.remove(row - col)