## Sudolko solver 
class Solution:    
      def solveSudoku(self, board):
        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        cell = [[] for _ in range(9)]  

        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    val = int(board[r][c])
                    rows[r].append(val)
                    cols[c].append(val)
                    cell[(r//3)*3 + (c//3)].append(val)

        solved = False

        def check(i, r, c):
            return (
                i not in rows[r] and
                i not in cols[c] and
                i not in cell[(r//3)*3 + (c//3)]
            )

        def backtrack(r, c):
            nonlocal solved
            if solved:
                return

            if board[r][c] == '.':
                for i in range(1, 10):
                    if check(i, r, c):
                        board[r][c] = str(i)
                        rows[r].append(i)
                        cols[c].append(i)
                        cell[(r//3)*3 + (c//3)].append(i)

                        if r == 8 and c == 8:
                            solved = True
                            return
                        elif c == 8:
                            backtrack(r+1, 0)
                        else:
                            backtrack(r, c+1)

                        if not solved:
                            board[r][c] = '.'
                            rows[r].remove(i)
                            cols[c].remove(i)
                            cell[(r//3)*3 + (c//3)].remove(i)

            else:
                if r == 8 and c == 8:
                    solved = True
                    return
                elif c == 8:
                    backtrack(r+1, 0)
                else:
                    backtrack(r, c+1)

        backtrack(0, 0)
        

       