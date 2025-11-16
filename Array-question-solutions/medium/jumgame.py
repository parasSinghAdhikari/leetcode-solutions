class Solution:
    def canJump(self, nums) -> bool:
        n= len(nums)
        if n==1:
            return True
        farther = 0
        curr  = 0
        for i in range(n-1):
            farther = max(farther,nums[i]+i)
            if curr ==i:
                curr =farther
            if curr >= n-1:
                return True
        return False