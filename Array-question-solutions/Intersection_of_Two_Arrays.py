#Time complexity O(n*n)
# Space complexity O(1) 
class Solution:
    def intersection(self, nums1, nums2) :
        ans=[]
        for num in nums1:
            if num in nums2 and num not in ans:
                ans.append(num)
        return ans
