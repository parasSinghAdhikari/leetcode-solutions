# approach by for loop (formula based is optimized approach)
# Time complexity O(n) 
class Solution:
    def totalMoney(self, n: int) -> int:
        money=0
        j=1
        mon = 2
        for i in range(1,n+1):
            money+=j
            j+=1
            if i%7==0:
                j=mon
                mon+=1
        return money 



        