class Solution:
    def arrayPairSum(self, nums) -> int:
        nums.sort()
        sums=0
        for i in range(0,len(nums),2):
            sums+=min(nums[i],nums[i+1])
        return sums

    
                
        