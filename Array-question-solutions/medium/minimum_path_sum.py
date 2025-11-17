# approach used DYanimic Programming 
# time complexity O(n*m)
# sapce complexity O(n*m)
class Solution:
    def minPathSum(self, grid) -> int:
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if i==0 and j==0:
                    continue
                if i>0:
                    sums1=grid[i][j]+grid[i-1][j]
                else:
                    sums1 = 2**32
                if j>0:
                    sums2 = grid[i][j]+grid[i][j-1]
                else:
                    sums2 = 2**32
                grid[i][j]=min(sums1,sums2)
        return grid[n-1][m-1]
                 
        