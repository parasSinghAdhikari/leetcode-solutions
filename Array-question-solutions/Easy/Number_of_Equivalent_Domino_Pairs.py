# Appraoch 1 using two nested loops not optimized
# time complexity O(n*N)
# sapce complxity O(1)
class Solution:
    def numEquivDominoPairs(self, dominoes) -> int:
        cnt = 0
        for i in range(1,len(dominoes)):
            for j in range(i-1,-1,-1):
                if ((dominoes[j][0]==dominoes[i][0]) and (dominoes[j][1]==dominoes[i][1])) or ((dominoes[j][0]==dominoes[i][1]) and (dominoes[j][1]==dominoes[i][0])):
                    cnt+=1
        return cnt  
    
# second Appraoch 
            
        