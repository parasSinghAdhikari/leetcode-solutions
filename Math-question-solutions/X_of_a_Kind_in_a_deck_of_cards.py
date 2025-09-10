# I use the approch of gcd (if any two numbers can be 
# divided into equal parts then its gcd >1 
# else it not be divided 

class Solution:
    def hasGroupsSizeX(self, deck) -> bool:
        def gcd(a,b):
            for i in range(min(a,b),1,-1):
                if a%i==0 and b%i==0:
                    return i
            return 1
        
        count ={}
        for num in deck:
            if num in count :
                count[num]+=1
            else:
                count[num] = 1
        
        g =-1
        for num in count.values():
            if g==-1:
                g = num
            else:
                g= gcd(g,num)
        return g>1

# if numbers  of  unique in deck = m
# If min in counts of m unique  = p 

# time complexity = O(n)+O(m*p) approximately  = O(n)

# space Complexity = O(m)