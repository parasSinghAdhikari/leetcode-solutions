# time complexity : O(N)
# space complexity : O(n)

class Solution:
    def countLargestGroup(self, n: int) -> int:
        dicts = {}
        for i in range(1,n+1):
            sums= 0
            while i>0:
                sums+=i%10
                i//=10
            if sums not in dicts:
                dicts[sums]=1
            else:
                dicts[sums]+=1
        maxi = max(list(dicts.values()))
        cnt = 0
        for val in list(dicts.values()):
            if val ==  maxi:
                cnt+=1
        return cnt 

        