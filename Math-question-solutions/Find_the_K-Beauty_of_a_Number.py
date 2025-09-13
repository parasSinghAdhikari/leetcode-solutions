class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        a = str(num)
        cnt=0
        for i in range(len(a)-k+1):
            temp = int(a[i:i+k])
            if temp!=0 and num%temp==0:
                cnt+=1
        return cnt