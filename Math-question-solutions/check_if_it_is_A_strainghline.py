# using area of triangle 
#time complexity O(n)
class Solution:
    def checkStraightLine(self, coordinates) -> bool:
        if len(coordinates)==2:
            return True
        for i in range(len(coordinates)-2):
            area = coordinates[i][0]*(coordinates[i+1][1]-coordinates[i+2][1]) + (coordinates[i+1][0]*(coordinates[i+2][1]-coordinates[i][1])) + (coordinates[i+2][0]*(coordinates[i][1]-coordinates[i+1][1])) 
            if area != 0:
                return False
        return True 
