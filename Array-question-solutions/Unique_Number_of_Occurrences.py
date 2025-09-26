class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        temp ={}
        for num in arr:
            if num in temp:
                temp[num]+=1
            else:
                temp[num]=1
        temp = list(temp.values())
        temp.sort()
        for i in range(1,len(temp)):
            if temp[i]==temp[i-1]:
                return False
        return True