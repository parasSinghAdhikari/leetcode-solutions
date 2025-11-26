class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n =len(needle)
        for i in range(0,len(haystack)):
            if needle==haystack[i:i+n]:
                return i
        return -1
        