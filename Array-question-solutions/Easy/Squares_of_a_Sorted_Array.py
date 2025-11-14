# time complexity O(n)
# space complexity O(1)
class Solution:
    def sortedSquares(self, nums):
        for i in range(len(nums)):
            if nums[i]>=0:
                break
        ans = []~
        j = i-1
        while j>=0 and i<len(nums):
            if nums[j]*nums[j] < nums[i]*nums[i]:
                ans.append(nums[j]*nums[j])
                j-=1
            else:
                ans.append(nums[i]*nums[i])
                i+=1
        while j>=0:
            ans.append(nums[j]*nums[j])
            j-=1
        while i<len(nums):
            ans.append(nums[i]*nums[i])
            i+=1
        return ans