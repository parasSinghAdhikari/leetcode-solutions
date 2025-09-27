# two pointer appraoch 
# Time complexity O(n+m)
class Solution:
    def countNegatives(self, grid) -> int:
        n = len(grid)
        m =  len(grid[0])
        r,c,cnt = n-1, 0,0
        while r>=0 and c<m:
            if grid[r][c]<0:
                r-=1
                cnt+=(m-c)
            else:
                c+=1
        return cnt
            
             

            