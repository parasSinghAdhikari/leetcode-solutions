class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        turn =0
        while True :
            x-=1
            y-=4
            if x<0 or y<0:
                break
            if turn==0:
                turn=1
            else:
                turn = 0
        if turn==0:
            return "Bob"
        return "Alice"

                



        