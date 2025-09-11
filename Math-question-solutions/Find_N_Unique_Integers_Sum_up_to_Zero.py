# generate the number -x and x and append both numbers in the list
# then if n is odd append 0 so the sum==0

#time complexity O(n)

class Solution:
    def sumZero(self, n: int):
        temp = []
        if n%2!=0:
            temp.append(0)
        
        count=n//2
        num=1
        while count > 0 : 
            temp.append(num)
            temp.append(-num)
            count-=1
            num+=1
            
        return temp

        