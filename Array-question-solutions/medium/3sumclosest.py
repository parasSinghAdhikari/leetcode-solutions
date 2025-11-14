# Approach used sorting and two pointer appraoch 
# time complexity O(n*n)
class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()
        n =len(nums)
        diff = 2**32
        ans=0
        for i in range(n):
            s,e= i+1,n-1
            while s<e:
                sums = nums[i]+nums[s]+nums[e]
                dif = abs(sums-target)
                if dif<diff:
                    diff =dif
                    ans= sums
                if sums<target:
                    s+=1
                else:
                    e-=1
        return ans 
        