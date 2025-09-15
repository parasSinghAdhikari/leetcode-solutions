# not optimization solution
# optimized appraoch is there by usng bitwise operator
class Solution:
    def kthCharacter(self, k: int) -> str:
        string ="abcdefghijklmnopqrstuvwxyz"

        word = 'ab'
        genS = 'b'
        while len(word)<k:
            new= ''
            for i in range(len(genS)):
                new += genS[i]+string[(string.index(genS[i])+1)%26]
            word+=new
            genS = new
        return word[k-1]

        
        