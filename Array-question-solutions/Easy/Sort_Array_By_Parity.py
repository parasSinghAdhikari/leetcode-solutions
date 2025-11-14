# appraoch used three pointer approach
# time complexity O(n)
# sapce complexity O(n)
class Solution:
    def sortArrayByParity(self, nums) :
        i,j,k = 0,0,len(nums)-1
        while j<k:
            if nums[i]%2!=0:
                nums[i],nums[k] = nums[k],nums[i]
                k-=1
            else:
                nums[i],nums[j] = nums[j],nums[i]
                j+=1
                i+=1
        return nums
        