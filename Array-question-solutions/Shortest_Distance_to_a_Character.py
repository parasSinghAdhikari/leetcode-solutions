class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        temp =[]
        for i in range(len(s)):
            if c ==s[i]:
                temp.append(i)
        print(temp,len(temp),len(s))
        ans = []
        j = 0
        for i in range(len(s)):
            if temp[j]< i and j<len(temp)-1:
                j+=1
            if j==0 :
                ans.append(abs(i-temp[j]))
            else:
                ans.append(min(abs(i-temp[j]),abs(i-temp[j-1])))
        return ans

        