# time complexity O(n*n)
#space complexity O(n)
class Solution:
    def sortByBits(self, arr):
        bits={}
        for num in arr:
            s = 0
            temp =num
            while num>0:
                if num&1==1:
                    s+=1
                num>>=1
            if temp not in bits:
                bits[temp] =s
                
        for i in range(1,len(arr)):
            j=i-1
            temp = arr[i]
            while j>=0 and ((bits[temp]<bits[arr[j]]) or (bits[temp]==bits[arr[j]] and temp<arr[j])) :
                arr[j+1] = arr[j]
                j-=1
            arr[j+1] = temp
        return arr 

        
        