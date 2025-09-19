class Solution:
    def calPoints(self, operations) -> int:
        ans= []
        for s in operations:
            if s[-1].isdigit():
                ans.append(int(s))
            elif s=='C':
                ans.pop()
            elif s=='D':
                ans.append(2*ans[-1])
            else:
                ans.append(ans[-1]+ans[-2])
        return sum(ans)
             
        