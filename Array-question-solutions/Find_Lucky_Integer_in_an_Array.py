# approach 1 by using sorting 
# time complexity O(nlog(n))
# sapce xomplexity O(1)
class Solution:
    def findLucky(self, arr) -> int:
        arr.sort()
        cnt= 1
        element = -1
        for i in range(1,len(arr)):
            if arr[i] == arr[i-1]:
                cnt+=1
            else:
                if cnt==arr[i-1]:
                    element = arr[i-1]
                cnt=1
        if cnt==arr[-1]:
            element =arr[-1]
        return element

# Approach 2 Using count array
# time complexity O(n)
# space complexity O(max(n))

class Solution:
    def findLucky(self, arr) -> int:
        maxi =max(arr)
        count = [0]*(maxi+1)

        for i in range(len(arr)):
            count[arr[i]]+=1
        
        for i in range(maxi,0,-1):
            if count[i]==i:
                return i
        return -1



        