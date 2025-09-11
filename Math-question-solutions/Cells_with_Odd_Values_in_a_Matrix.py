
#approach 1:
#time complexity O(L*(m+n))+O(n*m)
#space complxity O(n*m)

class Solution:
    def oddCells(self, m: int, n: int, indices) -> int:
        ans = [0 for _ in range(n*m)]
        
        for i in range(len(indices)):
            steps = indices[i][0]*n
            for j in range(steps,steps+n):
                ans[j]+=1
            for j in range(indices[i][1],n*m,n):
                ans[j]+=1
        cnt=0

        for num in ans:
            if num%2!=0:
                cnt+=1
        return cnt

# optimized approach  : I will do after When i good in this
            





        