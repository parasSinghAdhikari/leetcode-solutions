class Solution:
    def totalNQueens(self, n: int) -> int: 
        mat = [[0 for _ in range(n)]for _ in range(n)]
        count=0
        def check(i,j):
            r,c = i-1,j
            while  r>=0 :
                if mat[r][c]==1:
                    return False
                r-=1
            r,c = i-1,j-1
            while c>=0 :
                if mat[r][c]==1:
                    return False
                c-=1
                r-=1
            r,c = i-1,j+1
            while c<n :
                if mat[r][c]==1:
                    return False
                c+=1
                r-=1
            return True

        def backtrack(i):
            nonlocal count,mat
            if i==n:
                count+=1
                return 
            for j in range(n):
                if check(i,j):
                    mat[i][j] = 1
                    backtrack(i+1)
                    mat[i][j]=0
        backtrack(0)
        return count 