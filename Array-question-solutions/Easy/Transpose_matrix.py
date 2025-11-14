class Solution:
    def transpose(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        ans=[]
        for i in range (m):
            temp=[]
            for j in range(n):
                temp.append(matrix[j][i])
            ans.append(temp)
        return ans
        