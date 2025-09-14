# time complexity O(n(logn))
# space complexity O(log(n))
class Solution:
    def checkPrimeFrequency(self, nums) -> bool:
        def isprime(n):
            if n<=1:
                return False
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                    return False
            return True
        temp = []
        for i in range(len(nums)):
            if nums[i] not in temp:
                if isprime(nums.count(nums[i])):
                    return True
                temp.append(nums[i])
        return False
