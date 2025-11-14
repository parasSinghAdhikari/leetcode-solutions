class Solution:
    def maxKDistinct(self, nums, k: int):
        nums.sort(reverse=True)
        ans= [nums[0]]
        i =1
        while i < len(nums) and len(ans)<k:
            if nums[i]!=ans[-1]:
                ans.append(nums[i])
            i+=1
        return ans