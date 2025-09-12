# Approach go through 1 to n then check i and n-i number non zero
# time complexity O(n*log(n))
class Solution:
    def getNoZeroIntegers(self, n: int):
        ans = []
        i=1
        for i in range(1,n):
            a = i
            b = n-i
            while a>0 or b>0:
                if (a>0 and a%10==0) or (b>0 and b%10==0):
                    break
                a//=10
                b//=10
            if a==0 and b==0:
                ans.append(i)
                ans.append(n-i)
                break
        return ans

            
        