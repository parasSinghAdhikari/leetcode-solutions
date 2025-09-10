
# use formula of three points colinearity 

class Solution:
    def isBoomerang(self, points) -> bool:
        m1 = (points[0][0]-points[1][0])*(points[0][1]-points[2][1])
        m2 = (points[0][0]-points[2][0])*(points[0][1]-points[1][1])
        if m1 == m2 :
            return False
        return True
    