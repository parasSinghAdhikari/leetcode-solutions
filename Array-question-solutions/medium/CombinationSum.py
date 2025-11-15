# Approach used backtracking
class Solution:
    def combinationSum(self, candidates, target: int) :
        n=  len(candidates)
        def backtrack(temp,sums,idx,ans):
            if sums>target:
                return 
            if sums==target:
                ans.append(temp.copy())
                return 
            for i in range(idx,n):
                temp.append(candidates[i])
                sums+=candidates[i]
                backtrack(temp,sums,i,ans)
                temp.pop()
                sums-=candidates[i]
        ans = []
        backtrack([],0,0,ans)
        return ans


        