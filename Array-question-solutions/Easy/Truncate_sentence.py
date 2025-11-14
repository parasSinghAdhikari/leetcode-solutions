class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        cnt=0
        i=0
        while i<len(s):
            if s[i]==" ":
                cnt+=1
            if cnt==k:
                break
            i+=1
        return s[:i] 
        