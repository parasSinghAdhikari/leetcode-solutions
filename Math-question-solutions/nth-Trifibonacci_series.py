# approach same as fibonacci series 
# time complexity O(n)
# space complexity O(1)

class Solution:
    def tribonacci(self, n: int) -> int:
        t0 ,t1,t2= 0,1,1
        if n==0:
            return t0
        elif n==1:
            return t1
        elif n==2:
            return t2

        for i in range(3,n+1):
            nexts = t0+t1+t2
            t0 = t1
            t1 =t2
            t2 = nexts
        return t2

        