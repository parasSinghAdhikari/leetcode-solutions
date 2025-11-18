# time complexity O(n*m*2*l)
# sapce complexity O(n*m)
# but the solution can be optimized by Depth First Search
class Solution:
    def exist(self, board, word: str) -> bool:
        j=0
        n = len(board)
        m = len(board[0])
        temp = [1,-1,-1,1]
        dp = [[0 for j in range(m)]for i in range(n)]
        
        def backtrack(i,j,k,dp):
            if k==len(word):
                return True

            for p in range(4):
                l,r = i,j
                if p<2 :
                    l+=temp[p]
                else:
                    r+=temp[p]
                if 0<=l<n and 0<=r<m and dp[l][r]==0 and board[l][r]==word[k]:
                    dp[i][j] = 1
                    check = backtrack(l,r,k+1,dp)
                    if check:
                        return True
                    dp[i][j] = 0
            return False

        for i in range(n):
            for j in range(m):
                if board[i][j]==word[0]:
                    if backtrack(i,j,1,dp):
                        return True
        return False

# 
                

        