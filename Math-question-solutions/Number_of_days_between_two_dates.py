# Approch : find the number of days between the 1971 to date1 and to date2
# then give the difference beteween these

# time complexity O(n)

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def diff(date):
            monthdays = [31,28,31,30,31,30,31,31,30,31,30,31]
            year = int(date[:4])
            month = int(date[5:7])
            gap = int(date[8:])

            for i in range(1971,year):
                if (i%4==0 and i%100!=0) or i%400==0: 
                    gap += 366
                else:
                    gap += 365

            if month>2 and ((year%4==0 and year%100!=0) or year%400==0): 
                gap+= sum(monthdays[:month-1])+1
            else:    
                gap+= sum(monthdays[:month-1])
            return gap

        return abs(diff(date1)-diff(date2))