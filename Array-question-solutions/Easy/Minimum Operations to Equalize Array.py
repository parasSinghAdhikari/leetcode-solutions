class Solution:
    def minOperations(self, nums) -> int:

        for i in range(1,len(nums)):
            if nums[i] !=nums[i-1]:
                return 1
        return 0

# optimized approach 
class Solution:
    def minOperations(self, nums) -> int:
        x=len(set(nums))
        if x!=1:
            return 1
        else:
            return 0
        