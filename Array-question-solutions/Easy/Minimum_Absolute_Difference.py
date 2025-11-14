class Solution:
    def minimumAbsDifference(self, arr) :
        arr.sort()
        ans =[]
        mini = 2**32
        for i in range(len(arr)-1):
            diff = abs(arr[i]-arr[i+1]) 
            if diff<mini:
                ans = [[arr[i],arr[i+1]]]
                mini = diff
            elif diff==mini:
                ans.append([arr[i],arr[i+1]])
        return ans

        