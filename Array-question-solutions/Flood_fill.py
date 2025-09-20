# Time complexity O(n*n*4)
class Solution:
    def floodFill(self, image, sr: int, sc: int, color: int):
        n = len(image)
        m = len(image[0])
        def fill(r,c):
            check = image[r][c]
            image[r][c] = color
            temp= [-1,1,-1,1]
            for i in range(4):
                l,e = r,c
                if i<2:
                    l+=temp[i]
                else:
                    e+=temp[i]
                if l>=0 and l<n and e>=0 and e<m and image[l][e]==check and check!=color:
                    fill(l,e)
            return
        fill(sr,sc)
        return image
        