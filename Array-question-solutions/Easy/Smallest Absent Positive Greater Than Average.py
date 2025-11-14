class Solution:
    def smallestAbsent(self, nums) -> int:
        sums =sum(nums)
        if sums<0:
            sums= 0
        avg= sums//len(nums)+1

        while True:
            if avg not in nums:
                break
            avg+=1
        return avg
        