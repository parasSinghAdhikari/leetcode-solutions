# time complexity O(4^n)
# space complexity O(4^n)
class Solution:
    def letterCombinations(self, digits: str) :
        temp = ["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]

        ans =[""]
        for i in digits:
            n = len(ans)
            for j in range(n):
                for k in temp[int(i)-2]:
                    ans.append(ans[0]+k)
                ans.pop(0)
        return ans




        