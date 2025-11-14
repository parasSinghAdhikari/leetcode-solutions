class Solution:
    def shortestCompletingWord(self, licensePlate: str, words) -> str:
        letters = {}
        for i in licensePlate:
            if i.isalpha():
                i = i.lower()
                if i in letters:
                    letters[i] +=1
                else:
                    letters[i] =1
        print(letters)
        ans = ''
        for st in words:
            check = True
            for key ,value in letters.items():
                if key not in st or value > st.count(key):
                    check =False
                    break
            if check :
                if len(ans)==0 or  len(ans)>len(st):
                    ans= st   
        return ans


        