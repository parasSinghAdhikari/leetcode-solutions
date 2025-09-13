# Approach is used to find the square of two numbers add them and 
# find the square root of that addition number then 
# check it is a perfevt square or not 
# 
# Time complexity : O(n^2)
# 
# We can do little bit optimized by finding the square root using binary search  
class Solution:
    def countTriples(self, n: int) -> int:
        cnt=0
        for i in range(1,n):
            for j in range(i+1,n):
                check = (i*i+j*j)**0.5
                if int(check) ==check and check<=n:
                    cnt+=2 
        return cnt

            
        