class Solution:
    def countGoodRectangles(self, rectangles) -> int:
        cnt =0
        maxi = 0
        for i in range(len(rectangles)):
            temp = min(rectangles[i][0],rectangles[i][1])
            if maxi < temp:
                maxi = temp
                cnt=1
            elif maxi ==temp:
                cnt+=1
        return cnt
        