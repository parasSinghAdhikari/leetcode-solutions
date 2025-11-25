# approach used Siliding Window 
# time complexituy O(n*k)
# space complexity O(1)
class Solution:
    def findSubstring(self, s: str, words) :
        
        word_freq = {}
        for i in words:
            word_freq[i]= 1+word_freq.get(i,0)
        
        word_len = len(words[0])
        window_length = len(words)*word_len

        res =[]
        for i in range(len(s)-window_length+1):
            temp ={}
            j = i
            while j < i+window_length:
                curr = s[j:j+word_len]
                
                if curr not in word_freq:
                    break
                
                temp[curr] = temp.get(curr,0)+1
                if temp[curr]>word_freq[curr]:
                    break
                j+=word_len
            if j==i+window_length:
                res.append(i)
        return res

        