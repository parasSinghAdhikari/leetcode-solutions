class Solution:
    def canAliceWin(self, n: int) -> bool:
        turn = 1
        pick =10
        while n>=0:
            if n<pick:
                break
            n-=pick
            pick-=1
            if turn==0:
                turn=1
            else:
                turn =0
            
        return turn==0
        


        