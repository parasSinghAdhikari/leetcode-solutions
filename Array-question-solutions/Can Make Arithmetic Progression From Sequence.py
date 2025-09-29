# Appraoch used using sorting
# time complexity O(nlogn)
# space complexity O(1)
class Solution:
    def canMakeArithmeticProgression(self, arr) -> bool: 
        arr.sort()
        diff = arr[1]-arr[0]
        for i in range(2,len(arr)):
            if arr[i]-arr[i-1] !=diff:
                return False
        return True
    
# optimized approach using maximum and minimum
# time complexity O(n)
# Space complexity O(1)