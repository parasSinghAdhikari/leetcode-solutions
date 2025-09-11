#time complexity O(log(n))
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sums=0
        product =1 
        while n>0:
            sums+=n%10
            product*=n%10
            n=n//10
        return product-sums

        