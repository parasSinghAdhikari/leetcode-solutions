class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        average =-2**32-1
        j=0
        sums=0
        for i in range(len(nums)):
            sums+=nums[i]
            if i>=k-1:
                avg = sums/k
                sums-=nums[j]
                j+=1
                if avg>average:
                    average =avg
        return average  



        