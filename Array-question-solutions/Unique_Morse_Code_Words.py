# time complexity O(n*len(words))
# space complexity O(number(unique))
class Solution:
    def uniqueMorseRepresentations(self, words) -> int:
        temp = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ans = []
        for word in words:
            code = ''
            for l in word:
                code += temp[ord(l)-ord('a')]
            if code not in ans:
                ans.append(code)
        return  len(ans)
