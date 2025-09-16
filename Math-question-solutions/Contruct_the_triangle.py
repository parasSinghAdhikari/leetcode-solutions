class Solution:
    def constructRectangle(self, area: int):
        if area<=3:
            return [area,1]
        for l in range(int(area**0.5),area):
            if area%l==0 and l>=area//l:
                return [l,area//l]
        return [area,1]
        

            



        