class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        temp = [0]*n
        def nums(i,temp):
            if i ==n:
                return 1
            if int(s[i])==0:
                return 0
            if temp[i]!=0:
                return temp[i] 
            res = nums(i+1,temp)
            if i<n-1 and int(s[i:i+2])<=26:
                    res += nums(i+2,temp)
            temp[i] =res
            return temp[i]
        return nums(0,temp)
        
        