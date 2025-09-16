class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        monthDays =[0,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        arrivemonthA = int(arriveAlice[:2])
        leavemonthA = int(leaveAlice[:2])
        arrivedayA = int(arriveAlice[3:])
        leavedayA = int(leaveAlice[3:])
         
        arrivemonthB =int(arriveBob[:2])
        arrivedayB = int(arriveBob[3:])
        leavemonthB = int(leaveBob[:2])
        leavedayB = int(leaveBob[3:])

        startDayA = arrivedayA + sum(monthDays[:arrivemonthA])
        leaveDayA = leavedayA + sum(monthDays[:leavemonthA])
        startDayB = arrivedayB + sum(monthDays[:arrivemonthB])
        leaveDayB = leavedayB + sum(monthDays[:leavemonthB])
        
        cnt=0
        for i in range(min(startDayA,startDayB),max(leaveDayA,leaveDayB)+1): 
            if startDayA<=i and i<=leaveDayA and startDayB<=i and i<=leaveDayB:
                cnt+=1
        return cnt 

        

        
        