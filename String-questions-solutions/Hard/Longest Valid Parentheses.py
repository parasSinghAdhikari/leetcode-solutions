# approache used using Stack 
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        maxi = 0
        stack =[]
        for i in range(n):
            if s[i]=="(":
                stack.append(i)
            else:
                if len(stack)!=0:
                    if s[stack[-1]]=="(":
                        stack.pop(-1)
                    else:
                        stack.append(i)
                else:
                    stack.append(i)
        if len(stack)==0:
            return n
        i,j = n,0
        while len(stack)!=0:
            j = stack.pop(-1)
            maxi =max(maxi,i-j-1)
            i=j
        return max(maxi,i)

        