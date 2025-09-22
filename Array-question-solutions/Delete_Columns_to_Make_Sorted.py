class Solution:
    def minDeletionSize(self, strs) -> int:
        n = len(strs)
        m= len(strs[0])
        cnt=0
        for i in range(m):
            for j in range(n-1):
                if strs[j][i]>strs[j+1][i]:
                    cnt+=1
                    break
        return cnt

        