import math
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans =[]
        j,sums= 0,0
        for i in range(len(words)):
            n = len(words[i])
            sums+=n
            check = sums+(i-j)
            if check>maxWidth:
                temp = []
                gaps = i-j-1
                tg = maxWidth-(sums-n)
                if gaps==0:
                    temp.append(words[j]+(" "*tg))
                else:
                    while j<i:
                        if gaps==0:
                            l=0
                        else:
                            l = math.ceil(tg/gaps)
                        temp.append(words[j]+(" "*l))
                        tg-=l
                        gaps-=1
                        j+=1
                ans.append("".join(temp))
                j=i
                sums= n
        temp = " ".join(words[j:i+1])+" "*(maxWidth-sums-(i-j))
        ans.append(temp)
        return ans

 


        