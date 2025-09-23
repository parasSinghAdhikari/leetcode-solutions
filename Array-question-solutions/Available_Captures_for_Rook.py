class Solution:
    def numRookCaptures(self, board) -> int:
        temp = [1,-1,1,-1]
        
        for i in range(8):
            check = False
            for j in range(8):
                if board[i][j]=="R":
                    check = True
                    break
            if check:
                break

        cnt=0
        for m in range(0,4):
            k ,l = i,j
            if m<2:
                k+=temp[m]
                while board[k][l]=='.' and k>0 and k<7:
                    k+=temp[m]
            else:
                l+=temp[m]
                while board[k][l]=='.' and l>0 and l<7:
                    l+=temp[m]
            print(k,l)
            if board[k][l]=='p':
                cnt+=1
        return cnt
        