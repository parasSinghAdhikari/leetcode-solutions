class Solution:
    def findMissingAndRepeatedValues(self, grid) :
        n = len(grid)
        ans = [i for i in range(1,(n**2)+1)]

        for i in range(n):
            for j in range(n):
                if grid[i][j] in ans:
                    ans.remove(grid[i][j])
                else:
                    ans=[grid[i][j]]+ans
        return ans

        
        