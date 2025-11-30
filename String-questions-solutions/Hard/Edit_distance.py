# approached used Memoization
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n,m = len(word1),len(word2)
        dp = [[-1 for j in range(m)]for i in range(n)]
        def check(i,j,dp):
            if i<0:
                return j+1
            elif j<0:
                return i+1 
            if dp[i][j]!=-1:
                return dp[i][j]
            if word1[i]==word2[j]:
                dp[i][j] = check(i-1,j-1,dp)
                return dp[i][j]
            insert = 1+ check(i,j-1,dp)
            delete = 1+check(i-1,j,dp)
            update = 1+check(i-1,j-1,dp)
            dp[i][j] = min(update,delete,insert)
            return dp[i][j]
        return check(n-1,m-1,dp)  



            
        