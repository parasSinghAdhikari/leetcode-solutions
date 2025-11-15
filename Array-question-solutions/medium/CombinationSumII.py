class Solution:
   def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []
        n = len(candidates)

        def backtrack(start, temp, total):
            if total == target:
                res.append(temp[:])
                return
            if total > target:
                return

            for i in range(start, n):
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                temp.append(candidates[i])
                backtrack(i+1, temp, total + candidates[i])
                temp.pop()

        backtrack(0, [], 0)
        return res