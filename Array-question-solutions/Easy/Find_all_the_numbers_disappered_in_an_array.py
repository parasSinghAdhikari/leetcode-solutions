# OPTIMIZED APPROACH WITH USING THE SPACE 
# TIME COMPLEXITY o(n+n)

class Solution:
    def findDisappearedNumbers(self, nums) :
        ans =[]
        for i in range(len(nums)):
            if nums[i]>0:
                index = nums[i]-1
            else:
                index = nums[i]*-1-1
            if nums[index]>0:
                nums[index]*=-1

        for i in range(len(nums)) :
            if nums[i] >0:
                ans.append(i+1)
        return  ans    




        