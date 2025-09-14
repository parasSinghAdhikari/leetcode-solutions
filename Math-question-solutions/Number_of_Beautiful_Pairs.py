# time complexity (O(n^2))
class Solution:
    def countBeautifulPairs(self, nums) -> int:
        def gcd(a,b):
            for i in range(min(a,b),0,-1):
                if a%i==0 and b%i==0:
                    return i
        cnt=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if gcd(int(str(nums[i])[0]),int(str(nums[j])[-1]))==1:
                    cnt+=1
        return cnt 
        
        