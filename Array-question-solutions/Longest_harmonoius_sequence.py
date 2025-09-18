# appraoch i used using sorting or sliding window technique
# time complexity O(nlogn)
# space complexity O(1)

class Solution:
    def findLHS(self, nums) -> int:
        nums.sort()
        maxLen =0
        j=0
        for i in range(len(nums)):
            while nums[i]-nums[j]>1:
                j+=1
            if nums[i]-nums[j]==1 and maxLen<(i-j)+1:
                maxLen = (i-j)+1 
        return maxLen
                    
