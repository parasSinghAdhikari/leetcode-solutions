class Solution:
    def minOperations(self, logs) -> int:
        cnt=0
        for log in logs :
            if log=='../' and cnt >0:
                cnt-=1
            elif log!='./' and log!='../':
                cnt+=1
        return cnt