class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        temp  = [0 for i in range(256)]
        for i in t:
            temp[ord(i)]+=1

        i,j,mini,cnt,sindex=0,0,2**32,0,0
        while j < m:
            if temp[ord(s[j])] > 0:
                cnt += 1
            temp[ord(s[j])] -= 1
            j += 1

            while cnt == n:      
                if j - i < mini:
                    mini = j - i
                    sindex = i

                temp[ord(s[i])] += 1
                if temp[ord(s[i])] > 0:
                    cnt -= 1    
                i += 1

        if mini == 2**32:
            return ""        
        return s[sindex:sindex+mini]
                

         