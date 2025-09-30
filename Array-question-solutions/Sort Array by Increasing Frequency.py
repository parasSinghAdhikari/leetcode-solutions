class Solution:
    def frequencySort(self, nums) :
        temp = {}
        for num in nums:
            if num in temp:
                temp[num]+=1
            else:
                temp[num]=1

        for i in range(1,len(nums)):
            j = i-1
            front = nums[i]
            while j>=0 and (temp[nums[j]]>temp[front] or (temp[nums[j]]==temp[front] and nums[j]<front)):
                nums[j+1] = nums[j]
                j-=1
            nums[j+1] = front
        return nums
        