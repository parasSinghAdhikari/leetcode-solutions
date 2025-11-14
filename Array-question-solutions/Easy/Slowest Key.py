class Solution:
    def slowestKey(self, releaseTimes, keysPressed: str) -> str:
        n = len(releaseTimes)
        maxtime = releaseTimes[0]
        index = 0
        for i in range(1,n):
            temp = releaseTimes[i]-releaseTimes[i-1] 
            if temp>maxtime:
                maxtime = temp
                index = i
            elif temp==maxtime and keysPressed[i]>keysPressed[index]:
                index = i
        return keysPressed[index]


        