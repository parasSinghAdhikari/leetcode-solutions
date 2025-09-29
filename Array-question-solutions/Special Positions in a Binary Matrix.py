# Appraoch used using extrsa space 
# time complexity O(n*m)
# space complexity O(n+m)
class Solution:
    def numSpecial(self, mat) -> int:
        n ,m = len(mat),len(mat[0])
        r ,c = [0]*n,[0]*m 
        cnt=0
        for i in range(n):
            for j in range(m):
                if mat[i][j]==1:
                    r[i] += 1
                    c[j]+=1

        for i in range(n):
            for j in range(m):
                if mat[i][j]==1 and r[i]==1 and c[j]==1:
                    cnt+=1
        return cnt
                    
        