# time complexity O(c)
class Solution:
    def splitNum(self, num: int) -> int:
        ans= []
        while num>0:
            ans.append(num%10)
            num//=10
        
        ans.sort()
        
        mini1 = ''
        mini2 = ''
        for i in range(len(ans)):
            if i%2==0:
                mini1+=str(ans[i])
            else:
                mini2+=str(ans[i])
        return int(mini1)+int(mini2)
        