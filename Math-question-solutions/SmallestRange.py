class Solution:
    def smallestRangeI(self, nums, k) -> int:
        # n = len(nums)
        # if n == 1:
        #     return 0
        # nums[0] = nums[0] + k if nums[0] < nums[1] else nums[0] - k
        # for i in range(1, n):
        #     if nums[i] >= nums[i-1]:
        #         if nums[i] - nums[i-1] <= k:
        #             nums[i] -= (nums[i] - nums[i-1])
        #         else:
        #             nums[i] -= k
        #     else:
        #         if nums[i-1] - nums[i] <= k:
        #             nums[i] += (nums[i-1] - nums[i]) 
        #         else:
        #             nums[i] += k
        # print(nums)
        # return max(nums) - min(nums)
        # 
        # I Tried With above logic 1 condition is failed every time:
        # nums =  [5,6,4], k =5 ,Output 1 ,Expected = 0  


        # so i found this logic 
        #time colpexity  = O(n)
        #space complexity = O(1)
        return max(0,max(nums)-min(nums)-2*k)