class Solution:
    def recoverOrder(self, order, friends):
        temp ={}
        for i in range(len(order)):
            temp[order[i]] = i
        
        for i in range(1,len(friends)):
            j = i-1
            check = friends[i]
            while j>=0 and temp[check]<temp[friends[j]]:
                friends[j+1] = friends[j]
                j-=1
            friends[j+1] = check
        return friends

        