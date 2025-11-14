class Solution:
    def distanceBetweenBusStops(self, distance, start: int, destination: int) -> int:
        n= len(distance)
        d1,d2,i1,i2 = 0,0,start,start
        while i1!=destination :
            d1+=distance[i1%n]
            i1=(i1+1)%n
        while i2!=destination:
            if i2==0:
                i2 =n-1
            else:
                i2-=1
            d2+=distance[i2]
        return min(d1,d2)
        