# Time complexity O(n)
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        cnt=0
        for i in range(len(s)):
            if s[i]=='1':
                cnt+=1
        ans = '1'*(cnt-1)
        ans+='0'*(len(s)-cnt)
        ans+='1'
        return ans
        