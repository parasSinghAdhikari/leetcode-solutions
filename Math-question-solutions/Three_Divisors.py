# apppraoch i used here is the mathematical situation
# if the sqrt(num) is prime then it have exctly three divisiors
# Time complexity  : O(logn)
class Solution:
    def isThree(self, n: int) -> bool:
        def isPrime(n):
            if n<=1:
                return False
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                    return False
            return True

        check = n**0.5
        if int(check)==check and isPrime(check):
            return True
        return False 
            
        