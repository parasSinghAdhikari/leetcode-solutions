# time complexity O(log(n))
class Solution:
    def isFascinating(self, n: int) -> bool:
        num = int(str(n)+str(2*n)+str(3*n))
        print(num)
        temp = []
        while num>0:
            if num%10 ==0 or num%10 in temp :
                return False
            temp.append(num%10)
            num//=10
        return True
        