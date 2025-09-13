# using Binary search 
# time complexity O(n)
class Solution:
    def pivotInteger(self, n: int) -> int:
        s = 1
        e = n
        while s<=e:
            mid = (s+e)//2
            left = (mid*(mid+1))//2
            right = (mid+((n*(n+1))//2))-left
            if right == left :
                return mid
            elif left<right:
                s = mid+1
            else:
                e=mid-1
        return -1
        