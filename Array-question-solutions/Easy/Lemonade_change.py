class Solution:
    def lemonadeChange(self, bills) -> bool:
        temp = {5:0,10:0,20:0}
        for bill in bills:
            change = bill-5
            if change==5:
                if temp[5]==0:
                    return False
                temp[5] -=1
            elif change==15:
                if (temp[10]<1 and temp[5]<1):
                    return False
                elif (temp[10]>=1 and temp[5]>=1):
                    temp[10] -=1
                    temp[5]-=1
                elif temp[5]<3:
                    return False
                else:
                    temp[5]-=3
            temp[bill]+=1

        return True
            
                


        