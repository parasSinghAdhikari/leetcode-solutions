class Solution:
    def decompressRLElist(self, nums):
        i= 0
        ans=[]
        while i<len(nums):
            temp = [nums[i+1]]*nums[i]
            ans+=temp
            i+=2
        return ans
