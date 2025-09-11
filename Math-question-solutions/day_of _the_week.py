# Approach : For this approach i used to know what is the starting 
# weekday of the year 1971 which is "thrusday" so that is why i 
# initilize the ans with 4 and count the number of days till present 
# add with ans and after that ans%7 is the week day 
# 
# time complexity O(year-1971)
# space complexity O(1)

 
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        weekday = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
        monthdays = [31,28,31,30,31,30,31,31,30,31,30,31]

        ans = 4
        for i in range(1971,year):
            if (i%4==0 and i%100!=0) or i%400==0:
                ans+=366
            else:
                ans+=365
        if month>2 and ((year%4==0 and year%100!=0) or year%400==0):
            day+=sum(monthdays[:month-1])+1
        else:
            day+=sum(monthdays[:month-1])
        
        return weekday[(ans+day)%7]
        








        