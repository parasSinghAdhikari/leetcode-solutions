# Time complexity O(n)
# space complexity O(n)
class Solution:
    def findShortestSubArray(self, nums) -> int:
        count = {}
        first ={}
        degree =0
        j =0 
        maxlen = 0
        for i in range(len(nums)):
            a = nums[i]
            if a not in first:
                first[a] = i
            if a in count:
                count[a]+=1
            else:
                count[a] =1
            if count[a]>degree:
                degree = count[a]
                maxlen = (i-first[a])+1
            elif count[nums[i]]==degree:
                maxlen = min((i-first[a])+1,maxlen)
        return maxlen

            
        


        