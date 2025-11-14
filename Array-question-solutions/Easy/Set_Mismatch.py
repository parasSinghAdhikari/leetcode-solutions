# time complexity O(n)
# space complexity O(n)
class Solution:
    def findErrorNums(self, nums):
        n = len(nums)
        count  = [0 for i in range(n+1)]
        for i in range(n):
            count[nums[i]]+=1
        
        ans =[0,0]
        for i in range (1,n+1):
            if count[i]==2:
                ans[0]=i
            if count[i]==0:
                ans[1] = i
        return ans


        