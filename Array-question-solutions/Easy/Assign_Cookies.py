# approach is used using sorting Time ComplexityO(nlogn+mlogm)
class Solution:
    def findContentChildren(self, g, s) -> int:
        g.sort()
        s.sort()
     
        i,j=0,0
        cnt=0
        while i<len(s) and j<len(g):
            if g[j]<=s[i]:
                cnt+=1
                j+=1
            i+=1

        return cnt
            

        