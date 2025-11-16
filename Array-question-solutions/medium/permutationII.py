class Solution:
    def permuteUnique(self, nums) :
        def permute(nums):
            if len(nums)==1:
                return [nums] 
            temp =[]
            for i in range(len(nums)):
                curr = [nums[i]]
                rem = nums[:i]+nums[i+1:]
                for j in permute(rem):
                    if curr+j not in temp:
                        temp.append(curr+j)
            return temp
        return  permute(nums)