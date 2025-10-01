# Approach 1 is Brute Force using two loops
# time complexity O(n*k)
# space complexity O(n)
class Solution:
    def decrypt(self, code, k: int) :
        n  =len(code)
        temp = [0]*n

        if k ==0:
            return temp
        
        sign  = True if k<0 else False
        for i in range(n):
            cnt , loop, sums = i,k,0
            while loop!=0 :
                if sign:
                    cnt-=1
                    if cnt<0:
                        cnt=n-1
                    loop+=1
                else:
                    cnt+=1
                    loop-=1
                sums+=code[cnt%n]
            temp[i] = sums
        return temp

# approch 2 using sliding window 
# time complexity O(n)
# space complexity O(n)
class Solution:
    def decrypt(self, code, k: int) :
        n  =len(code)
        temp = [0]*n

        if k ==0:
            return temp
        if k>0:
            temp[0] = sums = sum(code[1:k+1])
            for i in range(1,n):
                r = (i+k)%n
                sums += -code[i] + code[r]
                temp[i] = sums
        if k<0:
            temp[0] = sums = sum(code[-1:k-1:-1])
            for i in range(1,n):
                r = (i-k)%n
                sums += -code[-i] + code[-r]
                temp[-i] = sums
        return temp