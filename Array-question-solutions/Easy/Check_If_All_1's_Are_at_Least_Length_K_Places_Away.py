class Solution:
    def kLengthApart(self, nums, k: int) -> bool:
        cnt = -1
        for i in range(len(nums)):
            if nums[i]==1:
                if cnt!=-1 and cnt<k:
                    return False
                cnt=0
            else:
                if cnt!=-1:
                    cnt+=1
        return True

        