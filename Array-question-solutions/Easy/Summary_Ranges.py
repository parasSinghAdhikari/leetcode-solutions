class Solution:
    def summaryRanges(self, nums) :
        n = len(nums)
        if n==0:
            return nums
        if n==1:
            return [str(nums[0])]
            
        ans =[]
        cnt = 0
        for i in range(n-1):
            if nums[i]+1==nums[i+1]:
                cnt +=1
            else:
                if cnt!=0:
                    ans.append(str(nums[i-cnt])+"->"+str(nums[i]))
                else:
                    ans.append(str(nums[i]))
                cnt= 0

        if cnt==0:
            ans.append(str(nums[i+1]))
        else:
            ans.append(str(nums[i+1-cnt])+"->"+str(nums[i+1]))
        return ans
                



