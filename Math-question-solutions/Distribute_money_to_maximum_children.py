# time complexity O(children)
class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if children>money:
            return -1
        
        k = children
        while k>0:
            if 8*k>money:
                k-=1
                continue
            leftmoney = money-8*k
            childrenleft = children-k
            if leftmoney>=childrenleft:
                if (childrenleft==0 and leftmoney!=0) or  (leftmoney==4 and childrenleft==1):
                    k-=1
                    continue
                return k
            k-=1
        return 0



        