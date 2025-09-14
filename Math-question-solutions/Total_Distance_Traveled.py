# time complexity O(mainTank)
class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        if mainTank<5:
            return mainTank*10
        total = 0
        while mainTank>=5 and additionalTank>0:
            total += 5*10
            mainTank = (mainTank-5)+1
            additionalTank-=1
        total+=(mainTank*10)
        return total 

        
        