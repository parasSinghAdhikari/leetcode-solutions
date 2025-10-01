class Solution:
    def maximumUnits(self, boxTypes, truckSize: int) -> int:
        boxTypes.sort(key=lambda x : x[1],reverse=True)
        sums =0
        i=0
        while i<len(boxTypes) and truckSize>0:
            if truckSize>=boxTypes[i][0]:
                sums+=boxTypes[i][0]*boxTypes[i][1]
            else:
                sums+=truckSize*boxTypes[i][1]
            truckSize-=boxTypes[i][0]
            i+=1
        return sums

            
        