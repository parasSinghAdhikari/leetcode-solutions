class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        temp ={}
        for i in range(len(nums)):
            if nums[i] in temp:
                if abs(temp[nums[i]]-i)<=k:
                    return True
                temp[nums[i]]=i 
            else:
                temp[nums[i]]=i
        return False
        