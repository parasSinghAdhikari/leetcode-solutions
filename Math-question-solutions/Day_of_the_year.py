# Approach 1 : time complexity  = O(nlog(n))+O(n) = approax(nlog(n))

class Solution:
    def dayOfYear(self, date: str) -> int:
        month = int(date[5:7])
        day = int(date[len(date)-2:])
        year = int(date[:4])
        if month <2:
            return day

        for i in range(month-1):
            if i==1:
                if (year%4==0 and year%100!=0) or year%400==0:
                    day+=29
                else:
                    day+=28
            elif i<=6:
                if i%2==0:
                    day+=31
                else:
                    day+=30
            else:
                if i%2==0:
                    day+=30
                else:
                    day+=31
        return day
                    
# optimized appraoch 2 : Time complexity O(1)
class Solution:
    def dayOfYear(self, date: str) -> int:
        months = [31,28,31,30,31,30,31,31,30,31,30,31]
        
        day = int(date[8:10])
        month = int(date[5:7])
        year = int(date[:4])

        if month>2 and ((year%4==0 and year%100!=0) or year%400==0):
            day+=sum(months[:month-1])+1
        else:
            day+=sum(months[:month-1])
        return day
