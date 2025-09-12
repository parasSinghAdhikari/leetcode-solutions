# Approach generate all the subset then tracverse through every subset 
# find xor and add them 

# time complexity O(2^n)
# space complexity O(2^n)

class Solution:
    def subsetXORSum(self, nums) -> int:
        ans=[[]]
        xor = 0
        for i in range(len(nums)):
            ans+=[j+[nums[i]] for j in ans]
        
        sums=0
        for arr in ans:
            xor =0
            for num in arr:
                xor^=num
            sums+=xor
        return sums 

# # optimized Approach using or bitwise operation
# . XOR Contribution of Each Bit:

# The XOR of a subset depends on the number of times each bit is set to 1 in the subset.
# If a bit is set in an odd number of elements in the subset, the XOR will have that bit set.
# The total sum is the sum of contributions from each bit position.
# 2 . OR Operation to Identify Active Bits:

# The bitwise OR of all numbers in the array (total |= num) tells us which bits are ever set in any number.
# For example, [1, 3] (binary 01 and 11) → OR result is 11 (binary), meaning bits 0 and 1 are set.
# 3 . Counting Subsets Where a Bit is Set in XOR:

# For a bit that is set in at least one number, it will be set in the XOR of exactly half of all subsets (i.e., 2^(n-1) subsets).
# This is because each bit independently appears in half of the subsets when considering all combinations.
            
class Solution:
    def subsetXORSum(self, nums) -> int:
        total = 0
        for num in nums:
            total |= num

        return total * (2**(len(nums) - 1))
            
            
                

                
