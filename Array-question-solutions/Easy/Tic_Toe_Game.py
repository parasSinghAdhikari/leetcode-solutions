class Solution:
    def tictactoe(self, moves) -> str:
        if len(moves)<=2:
            return "Pending"
        temp = [-1 for i in range(9)]
        for i in range(len(moves)):
            if i%2==0:
                temp[moves[i][0]*3+moves[i][1]] =1
            else:
                temp[moves[i][0]*3+moves[i][1]] =0
        for i in range(len(temp)): 
            if temp[i]!=-1:
                if i ==0 and ((temp[i]==temp[i+3] and temp[i+3]==temp[i+6]) or (temp[i]==temp[i+1] and temp[i+1]==temp[i+2]) or (temp[i]==temp[i+4] and temp[i+4]==temp[i+8])):
                    if temp[i]==1:
                        return "A"
                    else:
                        return "B"
                elif i ==1  and (temp[i]==temp[i+3] and temp[i+3]==temp[i+6]):
                    if temp[i]==1:
                        return "A"
                    else:
                        return "B"
                elif i==2 and ((temp[i]==temp[i+2] and temp[i+2]==temp[i+4]) or (temp[i]==temp[i+3] and temp[i+3]==temp[i+6])) :
                    if temp[i]==1:
                        return "A"
                    else:
                        return "B"
                elif (i==3 or i==6) and (temp[i]==temp[i+1] and temp[i+1]==temp[i+2]):
                    if temp[i]==1:
                        return "A"
                    else:
                        return "B"
        if len(moves)==9:
            return "Draw"
        return "Pending"