# time complexity O(n)
class Solution:
    def findLengthOfLCIS(self, nums) -> int:
        maxlen = 1
        j=0
        i=0
        while  i<len(nums)-1:
            if nums[i]>=nums[i+1]:
                if maxlen<(i-j)+1:
                    maxlen = (i-j)+1
                j=i+1
            i+=1
        if maxlen<(i-j)+1:
                maxlen = (i-j)+1
        return maxlen
        