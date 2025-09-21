class Solution:
    def fairCandySwap(self, aliceSizes, bobSizes):
        a = (sum(aliceSizes)-sum(bobSizes))//2
        alice = set(aliceSizes)
        for i in set(bobSizes):
            if a+i in alice:
                return [a+i,i] 

        