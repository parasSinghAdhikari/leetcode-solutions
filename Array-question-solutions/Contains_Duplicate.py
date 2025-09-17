# time complexity O(nlogn)
# sapce Complexity O(1)
class Solution:
    def containsDuplicate(self, nums) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] ==nums[i+1]:
                return True
        return False