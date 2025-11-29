class Solution:
    def isNumber(self, s: str) -> bool:
        checksign = True
        checkdot = True
        checke = True 
        for i in range(len(s)):
            if s[i]=="+"or s[i]=="-":
                if checksign:
                    checksign =False
                else:
                    return False
            elif s[i].isdigit() :
                checksign = False
            elif s[i]==".":
                if checkdot and ((i>0 and s[i-1].isdigit()) or (i<len(s)-1 and s[i+1].isdigit())):
                    checksign = False
                    checkdot =False
                else:
                    return False
            elif s[i]=="e" or s[i]=="E":
                if i>0 and checke and (s[i-1].isdigit() or s[i-1]=="." ):
                    checksign = True
                    checke = False
                    checkdot=False
                else:
                    return False
            elif s[i].isalpha():
                return False
        if not checke and not s[-1].isdigit():
            return False
        if  s[-1].isdigit() or s[-1]==".":
            return True
        return False