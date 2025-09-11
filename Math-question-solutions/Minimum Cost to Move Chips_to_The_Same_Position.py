# appraoch user odd parity even  parity 
class Solution:
    def minCostToMoveChips(self, position) -> int:
        costodd=0
        costeven = 0
        for i in range(len(position)):
            if position[i]%2!=0:
                costodd+=1
            else:
                costeven+=1
        
        return min(costodd,costeven)
#time complexity O(n)

         
        