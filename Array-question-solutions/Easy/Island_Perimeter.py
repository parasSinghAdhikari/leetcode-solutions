# time complexity O(n*m+o(4))
# space complexity O(4)
class Solution:
    def islandPerimeter(self, grid) -> int:
        peri = 0
        temp = [1,-1,1,-1]
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    for k in range(4):
                        l,r = i,j
                        if k<2:
                            l+=temp[k]
                        else:
                            r+=temp[k]
                        if (l>=0 and l<n) and (r>=0 and r<m):
                            if grid[l][r]==0:
                                peri+=1
                        else:
                            peri+=1
        return peri        
                    

        