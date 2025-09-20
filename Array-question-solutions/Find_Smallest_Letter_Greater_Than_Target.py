# time complexity O(log(n))
class Solution:
    def nextGreatestLetter(self, letters, target: str) -> str:
        target = ord(target)
        s = 0
        e = len(letters)-1
        index= 0
        while s<=e:
            mid=(s+e)//2
            if ord(letters[mid])-target<=0:
                s = mid+1
            else:
                index = mid
                e=mid-1
            
        return letters[index] 


        