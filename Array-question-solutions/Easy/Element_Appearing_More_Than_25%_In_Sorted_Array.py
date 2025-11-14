class Solution:
    def findSpecialInteger(self, arr) -> int:
        count = 1
        element = arr[0]
        maxcount = 1
        for i in range(1,len(arr)):
            if arr[i]==arr[i-1]:
                count+=1
            else:
                if count>maxcount:
                    element = arr[i-1]
                    maxcount = count
                count=1
        if maxcount<count:
            element =arr[i]
        return element