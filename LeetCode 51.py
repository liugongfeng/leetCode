class Solution:

    
    def solveNQueens(self, n):
        if n < 1:  return []
        self.result = []
        self.cols = set(); self.pie = set(); self.na = set()
        self.DFS(n, 0, [])
        # return self.result
        return self.generate(n)

    def DFS(self, n, row, cur_state):
        if row >= n:
            self.result.append(cur_state)
            return
        for col in range(n):
            if col in self.cols or row + col in self.pie or row - col in self.na:
                continue        #  <- go die!
            self.cols.add(col)
            self.pie.add(row + col)
            self.na.add(row - col)

            self.DFS(n, row + 1, cur_state + [col])

            self.cols.remove(col)
            self.pie.remove(row + col)
            self.na.remove(row - col)

    def generate(self, n):
        board = []
        for res in self.result:
            for i in res:
                board.append("." * i + "Q" + "." * (n - i - 1))
        return [board[i: i + n] for i in range(0, len(board), n)]

s = Solution()
result = s.solveNQueens(4)
print(result)