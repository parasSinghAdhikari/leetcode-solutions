class Solution:
    def restoreString(self, s: str, indices) -> str:
        temp= ['']*len(s)
        for i in range(len(s)):
            temp[indices[indices[i]]] = s[indices[i]]
        return "".join(temp)