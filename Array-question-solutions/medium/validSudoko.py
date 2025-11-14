class Solution:
    def isValidSudoku(self, board) -> bool: 
        col = [[] for j in range(9)]
        for i in range(9):
            row = []
            if i%3==0:
                cell = [[] for _ in range(3)]
            for j in range(9):
                if board[i][j]!='.':
                    if board[i][j] not in row and board[i][j] not in col[j] and  board[i][j] not in cell[j//3]:
                        row.append(board[i][j])
                        col[j].append(board[i][j])
                        cell[j//3].append(board[i][j])
                    else:
                        return False
        return True
