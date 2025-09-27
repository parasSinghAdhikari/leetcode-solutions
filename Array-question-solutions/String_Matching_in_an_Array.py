class Solution:
    def stringMatching(self, words) :
        ans = []
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                if len(words[i])!=len(words[j]):
                    if words[i] in words[j] and words[i] not in ans :
                        ans.append(words[i])
                    if words[j] in words[i] and words[j] not in ans:
                        ans.append(words[j])
        return ans
                    