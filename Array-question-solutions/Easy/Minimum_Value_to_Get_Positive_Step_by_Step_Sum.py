class Solution:
    def minStartValue(self, nums) -> int:
        # startValue = 1
        # while True:
        #     sums = startValue
        #     check =True
        #     for i in range(len(nums)):
        #         sums += nums[i]
        #         if sums<1:
        #             check =False
        #     if check:
        #         return startValue
        #     startValue+=1
        
        sums= 0
        prefixsum = 0
        for i in range(len(nums)):
            sums+=nums[i]
            if sums<prefixsum:
                prefixsum =sums
        return 1-prefixsum


        