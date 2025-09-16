# Approach time complexity O(n*n)
# space complexity O(1) the question tell me to do in place that is why the time complexity is higher
#  But i can reduce the time complexity to O(n) but space complexity to O(n)

class Solution:
    def removeElement(self, nums, val: int) -> int:
        cnt=0
        i=0
        while i< len(nums)-cnt:
            if nums[i]==val:
                cnt+=1
                for j in range(i,len(nums)-1):
                    nums[j]=nums[j+1]
                continue
            i+=1
        return len(nums)-cnt

        