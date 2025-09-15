class Solution:
    def convertDateToBinary(self, date: str) -> str:
        year  = int(date[:4])
        month = int(date[5:7])
        day = int(date[8:])
        ans =[year,month,day]

        for i in range(3):
            temp =''
            num = ans[i]
            while num>0:
                temp+=str(num%2)
                num//=2
            ans[i] =temp[::-1]
        return "-".join(ans)    

        
        