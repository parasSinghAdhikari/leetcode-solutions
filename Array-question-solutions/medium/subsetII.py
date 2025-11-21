# time complexity O(n*(2^n))
class Solution:
    def subsetsWithDup(self, nums) :
        nums.sort()
        ans=[[]]
        for i in nums:
            ans+=[j+[i] for j in ans if j+[i] not in ans]
        return ans 