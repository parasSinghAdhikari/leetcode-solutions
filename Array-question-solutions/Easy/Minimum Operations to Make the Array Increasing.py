class Solution:
    def minOperations(self, nums) -> int:
        cnt =0 
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                temp=(nums[i-1]-nums[i])+1
                nums[i] += temp
                cnt+=temp
        return cnt
        
        