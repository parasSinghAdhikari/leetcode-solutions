# time complexity O(n)
# space complexity O(1)
class Solution:
    def thirdMax(self, nums) -> int:    
        firstmax = -2**31-1
        secondmax = -2**31-1
        thirdmax = -2**31-1
        for num in nums:
            if num==firstmax or num == secondmax or num ==thirdmax:
                continue
            if num > firstmax:
                thirdmax =secondmax
                secondmax = firstmax
                firstmax = num
            elif num>secondmax:
                thirdmax = secondmax
                secondmax = num
            elif num>thirdmax:
                thirdmax = num
        
        if thirdmax>=-2**31:
            return thirdmax
        return firstmax