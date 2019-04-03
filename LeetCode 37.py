class Solution:

    def solveSudoku(self, board: list[list[str]]) -> None:
        if board is None or len(board[0]) == 0:
            return
        self.solve(board)

        
    def solve(self, board: list[list[str]]) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    for c in "123456789":
                        if self.isValid(board, i, j ,c):
                            board[i][j] = c
                            if self.solve(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False            

        return True    



    def isValid(self, board, row, col, c):
        for i in range(len(board)):
            if board[i][col] != '.' and board[i][col] == c:
                return False
            if board[row][i] != '.' and board[row][i] == c:
                return False

            if board[3*(row//3) + i//3][3*(col//3) + i%3] != '.' and \
                board[3*(row//3) + i//3][3*(col//3) + i%3] == c:

                return False

        return True                      