class Solution:
    def canBeEqual(self, target, arr) -> bool:
        maxi = max(arr)
        temp = [0]*(maxi+1)
        for num in arr:
            temp[num]+=1
      
        for num in target: 
            if num > maxi:
                return False
            temp[num]-=1 
        
        for i in range(maxi+1): 
            if temp[i]!=0:
                return False
        return True 
        
        