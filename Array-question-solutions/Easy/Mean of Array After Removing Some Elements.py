class Solution:
    def trimMean(self, arr) -> float:
        arr.sort()
        n = len(arr)
        top = n//20
        return sum(arr[top:n-top])/(n-top*2)

        