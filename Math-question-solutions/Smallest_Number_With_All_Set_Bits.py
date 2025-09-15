class Solution:
    def smallestNumber(self, n: int) -> int:
        i =0 
        while True:
            i+=1
            if 2**i>n:
                return 2**i-1


        