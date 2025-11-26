class Solution:
    def countAndSay(self, n: int) -> str:
        temp = "1"
        for  i in range(n-1):
            count = 0
            prev=temp[0]
            temp2=""
            for j in temp:
                if j!=prev:
                    temp2+=str(count)+prev
                    count=1
                    prev = j
                else:
                    count+=1
            temp2+=str(count)+prev
            temp =temp2            
        return temp
        