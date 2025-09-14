# Approach time complexity O(n*n)
#space complexity O(1)
class Solution:
    def areSimilar(self, mat, k: int) -> bool:
        n = len(mat[0])
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j]!=mat[i][(j+k)%n]:
                      return False
        return True