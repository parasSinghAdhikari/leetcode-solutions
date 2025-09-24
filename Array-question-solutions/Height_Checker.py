class Solution:
    def heightChecker(self, heights) -> int:
        temp = sorted(heights)
        cnt=0
        for i in range(len(heights)):
            if heights[i]!=temp[i]:
                cnt+=1 
        return cnt