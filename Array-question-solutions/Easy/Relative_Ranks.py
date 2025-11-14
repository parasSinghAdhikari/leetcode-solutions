# Appraoch 1 using the sorting 
#time complexity O(nlog(n)+n*n)  = O(n*n)
#space Complexity O(n)

class Solution:
    def findRelativeRanks(self, score) :
        temp= sorted(score,reverse=True)
        
        for i in range(len(score)):
            index = temp.index(score[i])
            if index+1 == 1:
                score[i]='Gold Medal'
            elif index+1 ==2:
                score[i]='Silver Medal'
            elif index+1==3:
                score[i]='Bronze Medal'
            else:
                score[i]=str(index+1)
        return score

# Approach 2 using hashing
# time complexity O(n+n+maxi) = appraoximately O(n)
# space complexity O(maxi(score))
class Solution:
    def findRelativeRanks(self, score):
        maxi = max(score)

        temp = [0 for _ in range(maxi+1)]

        for i in range(len(score)):
            temp[score[i]] = i+1
    
        place = 1
        for i in range(maxi,-1,-1):
            if temp[i]==0:
                continue
            index = temp[i]-1
            if place== 1:
                score[index]='Gold Medal'
            elif place ==2:
                score[index]='Silver Medal'
            elif place==3:
                score[index]='Bronze Medal'
            else:
                score[index]=str(place)
            place+=1
        return score



        

        