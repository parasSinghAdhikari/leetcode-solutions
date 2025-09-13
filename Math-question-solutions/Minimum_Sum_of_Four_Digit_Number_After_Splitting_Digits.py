# Approach is used that the We can use the two smallest digits out of the four as the digits found in the tens place respectively.
# time complexity O(1)

class Solution:
    def minimumSum(self, num: int) -> int:
        ans= []
        while num>0:
            ans.append(num%10)
            num//=10
        
        min1 = min(ans)
        ans.remove(min1)
        min2 =min(ans)
        ans.remove(min2)

        min1  = int(str(min1)+str(ans[0]))
        min2 = int(str(min2)+str(ans[1])) 

        return min1+min2
        


        