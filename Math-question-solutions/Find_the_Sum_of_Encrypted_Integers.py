class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            n = len(str(nums[i]))
            if n<2:
                continue
            digit= 0
            num = nums[i]
            while num>0:
                if digit<num%10:
                    digit = num%10
                num//=10
            nums[i] = int(str(digit)*(n))
        return sum(nums)
            
        
        