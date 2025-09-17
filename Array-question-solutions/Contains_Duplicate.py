# time complexity O(nlogn)
# sapce Complexity O(1)
class Solution:
    def containsDuplicate(self, nums) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] ==nums[i+1]:
                return True
        return False
    
# appraoch 2 timecomplexity O(n)
# space complexity O(1)

temp ={}
class Solution:
    def containsDuplicate(self, nums) -> bool:
        temp ={}
        for i in range(len(nums)):
            if nums[i] in temp:
                return False
            else:
                temp[nums[i]]+=1
        return True