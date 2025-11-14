# By using without the space 
# time complexity O(n*n)

class Solution:
    def findRestaurant(self, list1, list2):
        mini = 2**32
        ans =  []
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    if mini>j+i:
                        if len(ans)>0:
                            ans.pop()
                        ans.append(list1[i])
                        mini=j+i
                    elif mini==j+i:
                        ans.append(list1[i])
        return ans

# there is optimized appraoch where we can use of set and dictionary 
# time complexity O(n+m)
# space complexity O(n)




                
        