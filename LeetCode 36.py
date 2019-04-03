class Solution:
    def isValidSudoku(self, board):
        record = set()
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    cur = board[i][j]

                    if (i, cur) in record or (cur, j) in record or (i//3, j//3, cur) in record:
                        return False

                    record.add((i, cur))                        
                    record.add((cur, j))
                    record.add((i//3, j//3, cur))

        return True