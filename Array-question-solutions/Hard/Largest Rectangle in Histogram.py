class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        maxi = 0
        for i in range(len(heights)+1):
            currl = heights[i] if i<len(heights) else 0
            while len(s)>0 and currl<heights[s[-1]]:
                height = heights[s.pop(-1)]
                width = i-s[-1]-1 if len(s)>0 else i  
                maxi = max(maxi,height*width)   
            s.append(i)
        return maxi