class Solution:
    def generateMatrix(self, n: int) :
        ans = [[0 for i in range(n)]for j in range(n)]
        x , y ,dx,dy = 0,0,0,1
        for k in range(n*n):
            ans[x][y] = k+1
            if not 0<=x+dx<n or not 0<=y+dy<n or ans[x+dx][y+dy]!=0:
                dx,dy = dy,-dx
            x+=dx
            y+=dy
        return ans


        