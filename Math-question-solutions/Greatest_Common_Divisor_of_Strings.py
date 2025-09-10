# Approach i used here of same as of gcd of numbers
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str2) > len(str1):
            str1,str2 =str2,str1
        
        n = len(str1)
        
        for i in range(len(str2),0,-1):
            if  str2[0:i]*(n//i) == str1 and str2 == str2[0:i] * (len(str2) // i):
                return str2[0:i]
        return ""
            
# time complexity O(min(n,m))
#space complexity O(1)
        