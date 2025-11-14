# approach 1 Not optimized using binary search 
# time complexity O(n*n*logn)
# space compolexity O(1)
class Solution:
    def checkIfExist(self, arr) -> bool:
        arr.sort()
        n  = len(arr)
        for i in range(n):
            s ,e= 0,n-1
            while s<=e:
                m =(s+e)//2
                if arr[m]*2==arr[i] and m!=i:
                    return True
                elif arr[m]*2>arr[i]:
                    e = m-1
                else:
                    s=m+1
        return False

# appraoch 2 using hashset 
# time compleixty O(nlogn)
# space complexity O(unique(n))
class Solution:
    def checkIfExist(self, arr) -> bool:
        arr.sort()
        n  = len(arr)
        s  = set()
        for num in arr:
            if num*2 in s or  num/2 in s:
                return True
            s.add(num)
        return False