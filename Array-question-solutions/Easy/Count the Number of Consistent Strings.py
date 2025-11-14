# approach used using the check all the word in allowed presenmt or not
# time complexity O(n*26*m)
# Space complexity O(1)
# we can reduce the time complexity by using the hash set 
class Solution:
    def countConsistentStrings(self, allowed: str, words) -> int:
        cnt=0
        for word in words:
            check = True
            for i in word:
                if i not in allowed:
                    check =False
                    break
            if check:
                cnt+=1
        return cnt
        