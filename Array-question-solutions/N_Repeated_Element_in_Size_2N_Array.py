# sapce complexity O(n)
# time complexity O(1)
class Solution:
    def repeatedNTimes(self, nums) -> int:
        element = -1
        count=0
        for i in range(len(nums)-2):
            if nums[i]==nums[i+1] or nums[i]==nums[i+2]:
                return nums[i]
        return nums[-1]

        