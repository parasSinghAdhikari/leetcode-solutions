class Solution:
    def getMinDistance(self, nums, target: int, start: int) -> int:
        dist  = 2**32
        for i in range(len(nums)):
            if nums[i]==target:
                dist= min(dist,abs(i-start))
        return dist
        