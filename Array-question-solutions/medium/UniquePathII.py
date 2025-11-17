# approach used DYanimic Programming 
# time complexity O(n*m)
# sapce complexity O(n*m)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        if obstacleGrid[0][0]==1 or obstacleGrid[0][0]==1:
            return 0
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        
        dp = [[0 for _ in range(m)] for _ in range(n)]
        dp[0][0] =1
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j]==1:
                    dp[i][j]=0
                    continue
                if i>0:
                    dp[i][j]+=dp[i-1][j]
                if j>0:
                    dp[i][j]+=dp[i][j-1]
        return dp[n-1][m-1]

                

              

        