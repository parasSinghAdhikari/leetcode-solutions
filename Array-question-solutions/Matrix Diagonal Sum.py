class Solution:
    def diagonalSum(self, mat) -> int:
        n = len(mat)
        sums = 0
        for i in range(n):
            for j in range(n):
                if i==j or i+j+1 == n:
                    sums+=mat[i][j]
        return sums

        