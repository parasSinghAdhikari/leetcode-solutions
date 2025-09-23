class Solution:
    def canThreePartsEqualSum(self, arr) -> bool:
        sums = sum(arr)
        if sums%3!=0:
            return False
        sums =sums//3
        temp,cnt = 0,0
        for i in range(len(arr)):
            temp+=arr[i]
            if temp==sums:
                cnt+=1
                temp=0
            if cnt==3:
                return True
        return False