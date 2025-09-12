# Approach 
# time complexity(O(n*log(n)))
# space complexity O(n)

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        n = (highLimit-lowLimit)+1
        ans = {}
        for i in range(lowLimit,highLimit+1):
            sums =0
            while i>0:
                sums+=i%10
                i//=10
            if sums in ans:
                ans[sums]+=1
            else:
                ans[sums]=1
        
        return max(list(ans.values()))
        