class Solution:
    def nearestValidPoint(self, x: int, y: int, points) -> int:
        dis = 2**32
        index =-1
        for i in range(len(points)):
            if points[i][0]==x or points[i][1]==y:
                manhatten = abs(x-points[i][0])+abs(y-points[i][1])
                if dis>manhatten:
                    index = i
                    dis = manhatten
        return index   