# time complexity O(n)
class Solution:
    def findPoisonedDuration(self, timeSeries , duration) -> int:
        total = 0
        poisonSec = timeSeries[0]
        for i in  range(len(timeSeries)):
            if poisonSec>timeSeries[i]:
                total+=(timeSeries[i]+duration-poisonSec)
            else:
                total+=duration
            poisonSec = timeSeries[i]+duration
        return total


        