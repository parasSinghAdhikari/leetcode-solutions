# approach used hasing and sorting 
# time complexity O(n*k*logn)
# space complxity O(n*k)
class Solution:
    def groupAnagrams(self, strs) :
        temp={}
        for i in range(len(strs)):
            s= list(strs[i])
            s.sort()
            s = "".join(s)
            if s not in temp:
                temp[s] = [strs[i]]            
            else:
                temp[s].append(strs[i])
        return list(temp.values())


                

             




        