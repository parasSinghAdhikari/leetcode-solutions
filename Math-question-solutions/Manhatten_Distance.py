# NOt optimal Approach Optimal Is BFS we do when we back to the question
# approach 1: sorted by values of dictionary
class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        temp = {}
        for i in range(rows):
            for j in range(cols):
                distance = abs(i-rCenter)+abs(j-cCenter)
                temp[(i,j)] = distance
        temp = dict(sorted(temp.items(),key = lambda item : item[1]))
        return [key for key, _ in temp.items()]
                