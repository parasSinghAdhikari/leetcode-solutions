class Solution:
    def addToArrayForm(self, num, k: int):
        # approach 1 : time complexity O(n)
        # space complexity O(n)
        
        ans = []
        carry = 0
        i= len(num)-1
        while k>0 or i>=0:
            if i>=0:
                sums = num[i]+(k%10)+carry
            else:
                sums = (k%10)+carry
            if sums>=10:
                ans.append(sums%10)
                carry = sums//10
            else:
                ans.append(sums)
                carry=0
            i-=1
            k = k//10
        if carry>0:
            ans.append(carry)
        return ans[::-1]
        
        # appraoch 2 : without space o(1)

        # for i in range(len(num)-1,-1,-1):
        #     total = num[i] + k
        #     num[i] = total % 10
        #     k = total // 10 
        
        # while k>0:
        #     num = [k%10]+num
        #     k=k//10
        # return num

