class Solution:
    def findJudge(self, n: int, trust) -> int:
        person = [0 for j in range(n+1)]
        trusts = [0 for j in range(n+1)]

        for  s in trust:
            person[s[0]]+=1
            trusts[s[1]]+=1
        for j in range(1,n+1):
            if trusts[j]==n-1 and person[j]==0:
                return j
        return -1