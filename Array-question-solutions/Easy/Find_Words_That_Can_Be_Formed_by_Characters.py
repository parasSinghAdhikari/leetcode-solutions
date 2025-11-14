class Solution:
    def countCharacters(self, words, chars: str) -> int:
        temp = {}
        for c in chars:
            if c in temp:
                temp[c]+=1
            else:
                temp[c]=1
        ans = 0
        for w in words:
            check={}
            for l in w:
                if l not in check:
                    check[l]=1
                else:
                    check[l]+=1
            t = True
            for key,values in check.items():
                if key not in temp or values>temp[key]:
                    t =False
                    break
            if t :
                ans+=len(w) 
        return ans   
                  
        