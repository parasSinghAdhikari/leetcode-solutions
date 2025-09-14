# approach is used using Two loops
# time complexity O(n*log(n))
class Solution:
    def diagonalPrime(self, nums) -> int:
        def isprime(n):
            if n<=1:
                return False
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                    return False
            return True

        n = len(nums)
        m = len(nums[0])
        largest = 0
        for i in range(n):
            for j in range(m):
                if (i==j or i+j+1 == m) and isprime(nums[i][j]) and largest<nums[i][j]:
                    largest = nums[i][j]      
        return largest
                    
# optimized apporach using one loop and check prime
class Solution:
    def diagonalPrime(self, nums) -> int:
        def isprime(n):
            if n<=1:
                return False
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                    return False
            return True

        n = len(nums)
        largest = 0
        for i in range(n):
            if isprime(nums[i][i]) and largest<nums[i][i]:
                largest = nums[i][i]
            if isprime(nums[i][n-i-1]) and  largest<nums[i][n-i-1]:
                largest = nums[i][n-i-1]
        return largest
                    

        
        