# Time complexity O(high-low*logn)
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        cnt=0
        for i in range(low,high+1):
            n = len(str(i))
            if n%2!=0:
                continue
            sums =0
            digitcnt= 0
            while i>0:
                if digitcnt<n//2:
                    sums+=(i%10)
                else:
                    sums-=(i%10)
                i//=10
                digitcnt+=1 
            if sums==0:
                cnt+=1
        return cnt

        