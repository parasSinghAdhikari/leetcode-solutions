class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        ans =""
        while num1>0 and num2>0 and num3>0:
            ans+=str(min(num1%10,num2%10,num3%10))
            num1//=10
            num2//=10
            num3//=10
        return int(ans[::-1])
            

        
        