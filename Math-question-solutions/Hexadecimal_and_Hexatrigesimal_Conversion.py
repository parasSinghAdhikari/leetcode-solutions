# approach is used but not optimal 
class Solution:
    def concatHex36(self, n: int) -> str:
        hexa = {10:"A",11:"B",12:"C",13:"D",14:"E",15:"F",16:"G",17:"H",18:"I",19:"J",20:"K",21:"L",22:"M",23:"N",24:"O",25:"P",26:"Q",27:"R",28:"S",29:"T",30:"U",31:"V",32:"W",33:"X",34:"Y",35:"Z"}
        a = n**2
        b=n**3

        ans = []
        while a>0:
            digit = a%16
            if digit>=10:
                ans.append(hexa[digit])
            else:
                ans.append(str(digit))
            a//=16
        ans2 =[]
        while b>0:
            digit = b%36
            if digit>=10:
                ans2.append(hexa[digit])
            else:
                ans2.append(str(digit))
            b//=36
        ans = ans[::-1]+ans2[::-1]
        return "".join(ans)

        