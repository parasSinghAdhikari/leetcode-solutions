# time complexity O(n+n+o(spaceused))
# space complexity O(unique(words))
class Solution:
    def mostCommonWord(self, paragraph: str, ) -> str:
        temp ={}
        paragraph = paragraph.lower()
        word = ''
        for c in paragraph:
            if c.isalpha():
                word+=c
            if c==" " or c in "!?\',:." :
                if len(word)>0: 
                    if word in temp:
                        temp[word]+=1
                    else:
                        temp[word]=1
                    word= ''
        if len(word)>0: 
            if word in temp:
                temp[word]+=1
            else:
                temp[word]=1
            word= ''
        maxi =0
        for key, value in temp.items():
            if key in banned:
                continue
            if value>maxi:
                word=key
                maxi =value
        return word
            
        

        