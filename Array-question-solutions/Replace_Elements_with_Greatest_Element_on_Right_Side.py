class Solution:
    def replaceElements(self, arr):
        maxi = -1
        for i in range(len(arr)-1,-1,-1):
            temp =arr[i]
            arr[i] = maxi
            if maxi<temp:
                maxi= temp
        return arr

        

        