# Time complexity O(number of words*len(words))
# Sapce complexity O(number of words)
class Solution:
    def findWords(self, words):
        keyboard = ["qwertyuiop",'asdfghjkl',"zxcvbnm"]
        wordRow=[]
        ans =[]
        
        for word in words:
            for row in range(3):
                if word[0].lower() in keyboard[row]:
                    wordRow.append(row)
                    break

        for i in range(len(words)):
            check =True
            word = words[i].lower()[1:]
            for l in word:
                if l not in keyboard[wordRow[i]]:
                    check=False
            if check:
                ans.append(words[i])
        return ans  

        