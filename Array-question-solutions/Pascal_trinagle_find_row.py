# appraoch 1 By using the factorial 
# time complexity O(n*n)
class Solution:
    def getRow(self, rowIndex: int) :
        def fact(n):
            prod =1
            for i in range(1,n+1):
                prod*=i
            return prod
        
        ans = []
        for i in range(0,rowIndex+1):
            temp = fact(rowIndex)//(fact(rowIndex-i)*fact(i))
            ans.append(temp)
        return ans

# approac 2 optimized : using the previous value
#time complexity O(n)
class Solution:
    def getRow(self, rowIndex: int) :
        ans = [1]
        prev = 1
        for i in range(1,rowIndex+1):
            nexts = prev*(rowIndex-i+1)//i
            ans.append(nexts)
            prev = nexts
        return ans