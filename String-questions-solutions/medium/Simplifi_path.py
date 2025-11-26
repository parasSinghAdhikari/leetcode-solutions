class Solution:
    def simplifyPath(self, path: str) -> str:
        temp = path.split("/")
        temp2 = []
        for i in temp:
            if i=="." or i=="":
                continue
            elif i=="..": 
                if len(temp2)>0:
                    temp2.pop(-1)
            else:
                temp2.append(i)
        
        return "/"+"/".join(temp2)


        