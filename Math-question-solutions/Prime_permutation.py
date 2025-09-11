# apparoach : genrerate the using is prime and factorial
# time complexity: O(nlogn)

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def isprime(a):
            for i in range(2,int(a**0.5)+1):
                if a%i==0:
                    return False
            return True

        def perm(a):
            fact=1
            for i in range(2,a+1):
                fact*=i
            return fact
        
        cnt =0
        for i in range(2,n+1):
            if isprime(i):
                cnt+=1

        ans = perm(cnt)*perm(n-cnt)

        return ans%((10**9)+7)