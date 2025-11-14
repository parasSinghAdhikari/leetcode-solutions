class Solution:
    def arrayRankTransform(self, arr) :
        temp = sorted(arr)
        ranks = {}
        j = 1
        for i in range(len(temp)):
            if temp[i] not in ranks:
                ranks[temp[i]]=j
                j+=1

        for i in range(len(arr)):
            arr[i] = ranks[arr[i]]
        return arr

        