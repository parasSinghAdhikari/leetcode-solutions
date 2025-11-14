class Solution:
    def specialArray(self, nums) -> int:
        nums.sort()
        n = len(nums)
        for i in range(1,n+1):
            s,e = 0,n-1
            while s<=e:
                m = (s+e)//2
                if nums[m]>=i:
                    e= m-1
                else:
                    s=m+1
            if n-s==i:
                return i
        return -1

        