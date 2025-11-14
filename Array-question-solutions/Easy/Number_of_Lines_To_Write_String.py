# Time complexity O(n)
class Solution:
    def numberOfLines(self, widths, s: str) :
        n = len(s)

        l = 100
        cnt= 1
        for i in range (n):
            pixel = widths[ord(s[i])-ord('a')] 
            if l < pixel:
                cnt+=1
                l=100
            l -= pixel
        if l<0:
            return [cnt+1,widths[ord(s[i])-ord('a')]]

        return [cnt,100-l]
                 

        