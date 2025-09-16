class Solution:
    def minimumPushes(self, word: str) -> int:
        total =0
        j=1
        for i in range(len(word)):
            total+=j
            if i> 0 and i%8==0:
                j+=1
        return total+(j-1)
        