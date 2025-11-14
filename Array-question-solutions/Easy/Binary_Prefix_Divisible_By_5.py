class Solution:
    def prefixesDivBy5(self, nums):
        k=0
        n = len(nums)
        ans = [0 for i in range(n)]
        for i in range(n):
            k = (k<<1) | nums[i]
            ans[i] = (k%5==0)  
        return ans
        