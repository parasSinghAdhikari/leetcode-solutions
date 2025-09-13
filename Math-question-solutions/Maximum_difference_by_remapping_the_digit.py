# time complexity O(1)

class Solution:
    def minMaxDifference(self, num: int) -> int:
        maxi  = str(num)
        mini  = str(num)
        i = 0
        while i<len(maxi):
            if maxi[i] !='9':
                maxi=maxi.replace(maxi[i],'9')
                break
            i+=1
        i=0          
        while i<len(mini):
            if mini[i] !='0':
                mini= mini.replace(mini[i],'0')
                break
            i+=1
        return int(maxi) - int(mini)
        
