class Solution:
    def restoreIpAddresses(self, s: str) :
        n = len(s)
        ans = []
        def check(i,temp):
            nonlocal ans
            if len(temp)==4 and i==n:
                ans.append(".".join(temp))
                return
            if len(temp)==4 or i==n:
                return
            temp.append(s[i])
            check(i+1,temp)
            if i<n-1 and s[i]!= "0" :
                temp[-1] = s[i:i+2]
                check(i+2,temp)
            if i<n-2 and s[i]!= "0" and int(s[i:i+3])<=255:
                temp[-1] = s[i:i+3]
                check(i+3,temp)
            temp.pop(-1)
        check(0,[])
        return ans
            

    
                 
        