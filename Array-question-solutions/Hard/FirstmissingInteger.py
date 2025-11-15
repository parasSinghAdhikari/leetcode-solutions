class Solution:
    def firstMissingPositive(self, nums) -> int:
        n=len(nums)
        for i in range(n):
            while 0<nums[i]<=n and i!=nums[i]-1:
                nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
  
        for i in range(n):
            if  nums[i]-1!=i:
                return i+1
        return n+1

            
