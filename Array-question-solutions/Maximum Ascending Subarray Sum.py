class Solution:
    def maxAscendingSum(self, nums) -> int:
        sums =nums[0]
        maxi = -1
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                maxi = max(maxi,sums)
                sums =0
            sums+=nums[i]
        maxi = max(sums,maxi)
        return maxi
                
        