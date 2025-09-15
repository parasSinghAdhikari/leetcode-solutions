# approached 1 not optimized
# time complexity O(n*n)

class Solution:
    def countPartitions(self, nums) -> int:
        cnt=0
        for i in range(len(nums)-1):
            if (sum(nums[:i+1])-sum(nums[i+1:]))%2==0:
                cnt+=1
        return cnt

# appraoach 2 optimized approach 
# time complexity O(n)
class Solution:
    def countPartitions(self, nums) -> int:
        r = sum(nums)
        l =0
        cnt= 0

        for i in range(len(nums)-1):
            if (l+nums[i] - (r-nums[i]))%2==0:
                cnt+=1
        return cnt
        