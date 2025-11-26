# Approached Used Recursion and memoization
# time complexity O(n*m)
# space complexity O(n*m)+ O(n+m)(recursion space stack)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n,m = len(p), len(s)
        dp =[[-1 for j in range(m)] for i in range(n)]
        
        def f(i,j,dp):
            if i<0 and j<0:
                return True
            elif i<0 and j>=0:
                return False
            elif i>=0 and j<0:
                for i in p[:i+1]:
                    if i !="*":
                        return False
                return True

            if dp[i][j]!=-1:
                return dp[i][j]
            
            if p[i]=="*":
                dp[i][j] = f(i,j-1,dp) or f(i-1,j,dp)
                return dp[i][j]
            elif p[i]==s[j] or p[i]=="?":
                dp[i][j]=f(i-1,j-1,dp)
                return dp[i][j]
            return False

        return f(n-1,m-1,dp)
        
# second Approached optimized using Tabulation  
# time complexity O(n*n)
# space complexity O(n*m)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n,m = len(p), len(s)
        dp =[[False for j in range(m+1)] for i in range(n+1)]
        dp[0][0] = True

        for j in range(1,m+1):
            dp[0][j]  = False

        for  i in range(1,n+1):
            flag = True
            for j in range(1,i+1):
                if p[j-1] !="*":
                    flag= False
            dp[i][0] = flag

        for i in range(1,n+1):
            for j in range(1,m+1):
                if p[i-1]=="*":
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                elif p[i-1]==s[j-1] or p[i-1]=="?":
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j] = False
        
        return dp[n][m]
        