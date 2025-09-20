# time complexity O(n)
class Solution:
    def pivotIndex(self, nums) -> int:
        totalsums = sum(nums)
        sums = 0
        for i in range(0,len(nums)):
            if sums==(totalsums-sums-nums[i]):
                return i
            sums+=nums[i]
        return -1
