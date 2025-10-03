class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        temp =[0]*10
        while n>0:
            temp[n%10] +=1
            n//=10
        
        freq = 2**32
        digit = -1
        for i in range(10):
            if temp[i]!=0 and freq>temp[i] :
                digit = i
                freq = temp[i]
        return digit

        