# approach using first go in diagonal then horizontally then go verticaly
# run above for all points 
# Brute force approach 
class Solution:
    def minTimeToVisitAllPoints(self, points) -> int:
        # time=0
        # for i in range(len(points)-1):
        #     x  = points[i][0]
        #     y = points[i][1]
        #     x1,y1 = points[i+1][0],points[i+1][1]
        #     while x !=x1 and y!=y1:
        #         if x < x1:
        #             x+=1
        #         else:
        #             x-=1
        #         if y<y1:
        #             y+=1
        #         else:
        #             y-=1
        #         time+=1
        #     while x!=x1:
        #         if x < x1:
        #             x+=1
        #         else:
        #             x-=1
        #         time+=1
        #     while y!=y1:
        #         if y<y1:
        #             y+=1
        #         else:
        #             y-=1
        #         time+=1
        # return time
    
# optimized approoach : using formula 
# max(abs(x-x1),abs(y-y1)) done
# time complexity O(n)

        time=0
        for i in range(len(points)-1):
            x  = points[i][0]
            y = points[i][1]
            x1,y1 = points[i+1][0],points[i+1][1]
            time+=max(abs(x-x1),abs(y-y1))
        return time
            



        