# Approach 1 using sorting
# time complexity O(nlogn)
# space complexity O(1)
class Solution:
    def maxProduct(self, nums) -> int:
        nums.sort()
        return (nums[-2]-1)*(nums[-1]-1)
    
# approach 2 by finding out largest ans second largest element
# time complexity O(n)
#spacecomplexity O(1)
        