# appraoch is used by me using insertion sort time complexityO(n*n)
# Space complexity O(1)
# Not so optimized but done by me 
class Solution:
    def relativeSortArray(self, arr1, arr2):
        temp= {}
        for i in range(len(arr2)):
            temp[arr2[i]] = i

        for i in range(1,len(arr1)):
            j = i-1
            tar = arr1[i]
            while j>=0  and ((tar in temp and arr1[j] in temp and temp[tar] < temp[arr1[j]]) or (arr1[j] not in temp and tar in temp)):
                arr1[j+1] = arr1[j] 
                j-=1
            arr1[j+1] = tar
            while j>=0 and arr1[j] not in temp and tar not in temp and arr1[j]>tar:
                arr1[j+1] = arr1[j] 
                j-=1
            arr1[j+1] = tar    
        return arr1

            
             
            

        

        