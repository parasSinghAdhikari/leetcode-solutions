# approach 1 brute force using two loops
# time comlexity O(n*(n+m))
# space complexity O(1)
class Solution:
    def luckyNumbers(self, matrix) :
        n =len(matrix)
        m =len(matrix[0])
        ans =[]
        for i in range(n):
            c =0
            mini = matrix[i][0]
            for j in range(1,m):
                if matrix[i][j]<mini:
                    mini = matrix[i][j]
                    c = j
            maxi = matrix[i][c]
            check=True
            for k in range(n):
                if matrix[k][c]>maxi:
                    check =False
            if check:
                ans.append(maxi)
        return ans

# appraoch 2 using space
# time complexity(O(n*n))
# sapce complexity O(n+m)

class Solution:
    def luckyNumbers(self, matrix):
        n ,m=len(matrix),len(matrix[0])
        cmax,rmin,ans = [],[],[]

        for i in range(n):
            rmin.append(min(matrix[i]))

        for i in range(m):
            maxi = matrix[0][i]
            for j in range(1,n):
                maxi = max(maxi,matrix[j][i])
            cmax.append(maxi)
      
        for i in range(n):
            if rmin[i] in cmax:
                ans.append(rmin[i])

        return ans


