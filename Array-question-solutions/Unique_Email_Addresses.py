
class Solution:
    def numUniqueEmails(self, emails) -> int:
        temp =[]
        for email in emails:
            s = ''
            i,c=0,True 
            while i < len(email):
                d = email[i]
                if d=='@':
                    break
                elif d=='.':
                    i+=1
                    continue
                elif d=='+':
                    c = False
                if c:
                    s +=d 
                i+=1
            s+=email[i:]
            if s not in temp:
                temp.append(s)
        print(temp)
        return len(temp)