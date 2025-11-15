class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==1:
            return [nums] 
        temp =[]
        for i in range(len(nums)):
            curr = [nums[i]]
            rem = nums[:i]+nums[i+1:]
            for j in self.permute(rem):
                temp.append(curr+j)
        return temp          
                
        


        