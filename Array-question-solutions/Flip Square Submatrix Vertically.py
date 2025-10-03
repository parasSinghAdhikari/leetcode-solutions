class Solution:
    def reverseSubmatrix(self, grid, x: int, y: int, k: int) :
        s =x
        e = x+k-1
        while s<e:
            for i in range(y,y+k):
                grid[s][i],grid[e][i]= grid[e][i],grid[s][i]
            s+=1
            e-=1
        return grid 
        