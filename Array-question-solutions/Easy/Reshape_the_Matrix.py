class Solution:
    def matrixReshape(self, mat, r: int, c: int) :
        n =len(mat)
        m = len(mat[0])

        if r*c!=n*m:
            return mat 
        
        i = 0
        j = 0
        ans =[]
        for _ in range(r):
            temp=[]
            for _ in range(c):
                temp.append(mat[i][j])
                if j<m-1:
                    j+=1
                else:
                    j=0
                    i+=1
            ans.append(temp)
        return ans


        