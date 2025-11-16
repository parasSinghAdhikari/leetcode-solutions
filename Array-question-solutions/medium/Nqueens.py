class Solution:
    def solveNQueens(self, n: int) :
        temp = [["." for j in range(n)]for i in range(n)]
        ans =[]
        def check(i,j):
            d1,d2 =j-1,j+1
            r = i-1
            while r>=0:
                if temp[r][j]=="Q":
                    return False
                r-=1
            
            r=i-1
            while d1>=0 and r>=0:
                if temp[r][d1]=="Q":
                    return False
                d1-=1
                r-=1
            r=i-1
            while d2<n and r>=0:
                if temp[r][d2]=="Q":
                    return False
                d2+=1
                r-=1
            return True
            
        def backtrack(i):
            if i==n:
                temp2 = []
                for j in range(n):
                    temp2.append("".join(temp[j]))
                ans.append(temp2)
                return 
            for j in range(n):
                if check(i,j):
                    temp[i][j] = "Q"
                    backtrack(i+1)
                    temp[i][j] = "."
        backtrack(0)
        return ans
          
        