class Solution:
    def jump(self, nums) -> int:
        n=len(nums)
        farther=0
        current= 0
        jumps=0
        for i in range(n-1):
            farther = max(farther,nums[i]+i)
            if i==current:
                jumps+=1
                current =farther
        return jumps






        