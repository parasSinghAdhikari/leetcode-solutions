class Solution:
    def isMonotonic(self, nums) -> bool:
        check = -1
        for i in range(1,len(nums)):
            if check == -1:
                if nums[i-1]>nums[i]:
                    check=1
                elif nums[i-1]<nums[i]:
                    check =0
            elif check == 0:
                if nums[i-1]>nums[i]:
                    return False
            else:
                if nums[i-1]<nums[i]:
                    return False
        return True
        