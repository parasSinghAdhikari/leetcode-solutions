class Solution:
    def maxLength(self, nums) -> int:
        def gcd(a,b):
            for i in range(min(a,b),1,-1):
                if a%i==0 and b%i==0:
                    return i
            return 1
        
        def lcm(a,b):
            lcm =max(a,b)
            while True:
                if lcm%a==0 and lcm%b==0 :
                    return lcm
                lcm+=1
        
        maxL = 0
        for i in range(len(nums)):
            j=i+1
            currgcd = nums[i]
            currLcm = nums[i]
            currPro = nums[i]
            while j<len(nums) :
                currPro*= nums[j]
                currgcd = gcd(currgcd,nums[j])
                currLcm = lcm(currLcm,nums[j])

                if currgcd*currLcm==currPro:
                    maxL = max(maxL,j-i+1)
                j+=1
        return maxL
