class Solution:
    def maximum69Number (self, num: int) -> int:
        temp = []
        num = str(num)
        cnt=0
        for i in range(len(num)):
            if cnt==0 and num[i]=="6":
                temp.append("9")
                cnt=1
            else:
                temp.append(num[i])
        return int("".join(temp))
        