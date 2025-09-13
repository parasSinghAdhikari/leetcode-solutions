# The question can be done by using the o(n)
# But i fin dthe solution using mathematical formula O(1)

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
    
        t = time//(n-1)
        if t%2==0:
            return time%(n-1)+1
        else:
            return (n-time%(n-1))
        