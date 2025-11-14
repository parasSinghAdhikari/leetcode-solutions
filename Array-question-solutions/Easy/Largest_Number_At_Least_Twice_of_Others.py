class Solution:
    def dominantIndex(self, nums) -> int:
        maxi =max(nums)
        index = -1
        for i in range(len(nums)):
            if nums[i]==maxi:
                index=i
                continue
            if nums[i]*2>maxi:
                return -1
        return index
        