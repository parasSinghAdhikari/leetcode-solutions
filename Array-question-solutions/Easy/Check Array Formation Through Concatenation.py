class Solution:
    def canFormArray(self, arr, pieces) -> bool:
        temp ={}
        temp2 =[]
        for i in pieces:
            temp[i[0]]=i
        
        for i in arr:
            if i in temp:
                temp2+=temp[i]
        return temp2==arr


        return False

        