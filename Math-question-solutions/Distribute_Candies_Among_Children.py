# time complexity O(n^2)
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        cnt=0
        for i in range(0,limit+1):
            for j in range(0,limit+1):
                if i+j<=n and n-(i+j)<=limit :
                    cnt+=1
        return cnt
