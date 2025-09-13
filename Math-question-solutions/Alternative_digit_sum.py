class Solution:
    def alternateDigitSum(self, n: int) -> int:
        l = len(str(n))
        sums =0
        if l%2==0:
            cnt=1
        else:
            cnt=0
        while n >0:
            if cnt%2==0:
                sums+=(n%10)
            else:
                sums-=(n%10)
            n//=10
            cnt+=1
        return sums