# time complexity O(n)
# space complexity O(n)
# not optimized
class Solution:
    def getSneakyNumbers(self, nums) :
        temp ={}
        for i in range(len(nums)):
            if nums[i] in temp:
                temp[nums[i]]+=1
            else:
                temp[nums[i]] =1
        ans =[]
        for key, values in temp.items():
            if values==2:
                ans.append(key)
        return ans
# there is a optimized version using quadratic equation and 
# sumof square and sum of numbers        