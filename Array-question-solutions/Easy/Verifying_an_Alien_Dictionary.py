class Solution:
    def isAlienSorted(self, words, order: str) -> bool:
        for i in range(len(words)-1):
            check = 0
            n = len(words[i])
            m = len(words[i+1])
            for j in range(min(n,m)):
                index1 = order.index(words[i][j]) 
                index2 = order.index(words[i+1][j])
                if index1<index2:
                    check=1
                    break
                elif index1>index2:
                    return False
            if n>m and check == 0:
                return False
        return True        