# Time colpexity O(n*n)
# space complexity O(n)
class Solution:
    def shiftGrid(self, grid, k: int):
        n = len(grid)
        m = len(grid[0])
        ans= [grid[i][j] for i in range(n) for j in range(m)]
        s = n*m
        temp = ans[s-(k%s):][::-1]
        ans = ans[:s-(k%s)][::-1]+temp
        ans =ans[::-1]

        k= 0 
        for i in range(n):
            for j in range(m):
                grid[i][j] = ans[k]
                k+=1
        return grid
        
# Time complexity O(n*n*k)
# Space complexity O(1)
class Solution:
    def shiftGrid(self, grid, k: int):
        n = len(grid)
        m = len(grid[0])

        k= k%(n*m)
        if k==0:
            return grid
            
        while k>0:
            temp = grid[n-1][m-1]
            for i in range(n-1,-1,-1):
                for j in range(m-1,-1,-1):
                    if i==0 and j==0:
                        continue
                    if j==0:
                        grid[i][j] = grid[i-1][m-1]
                    else:
                        grid[i][j] = grid[i][j-1]
            grid[0][0] = temp
            k-=1
        
        return grid


        
