# Not a good Apparach but done by me in O(n) time complexity 
class Solution:
    def validMountainArray(self, arr) -> bool:
        n = len(arr)
        if n<=2 or arr[0]>=arr[1]:
            return False
        check = 0
        change = 0
        for i in range(1,n):
            if change==-1:
                if arr[i-1]<=arr[i]:
                    return False
            elif check==0:
                if arr[i-1]==arr[i]:
                    return False
                if arr[i-1]>arr[i]:
                    check=1
                    change= -1
            else:
                if arr[i-1]==arr[i]:
                    return False
        if change==0:
            return False
        return True
                




        