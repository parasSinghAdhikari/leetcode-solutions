# i used Three Approaches 
class Solution:
    def largestPerimeter(self, nums) -> int:
        n = len(nums)
        # largest = 0
        # 1st : timecomplexity(O(n^3)) 
        # for i in range(n):
        #     for j in range(i+1,n):
        #         for k in range(j+1,n):
        #             if nums[i]+nums[j]>nums[k] and nums[k]+nums[j]>nums[i] and nums[k]+nums[i]>nums[j] and largest<nums[i]+nums[j]+nums[k]:
        #                 largest = nums[i]+nums[j]+nums[k]
        # return largest

        # 2nd : Two pointer approach 
        # time complexity O(n^2log(n))

        # nums.sort()
        # for i in range(n):
        #     s= i+1
        #     e = n-1
        #     while s<e:
        #         if nums[i]+nums[s]>nums[e] and nums[s]+nums[e]>nums[i] and nums[e]+nums[i]>nums[s] and largest<nums[i]+nums[s]+nums[e]:
        #             largest= nums[i]+nums[s]+nums[e]
        #             s+=1
        #         else:
        #             e-=1
        # return largest

        # time complexity O(nlogn) 
        nums.sort(reverse=True)
        for i in range(n-2):
            if nums[i]<nums[i+1]+nums[i+2]:
                return nums[i]+nums[i+1]+nums[i+2]
        return 0 
        

