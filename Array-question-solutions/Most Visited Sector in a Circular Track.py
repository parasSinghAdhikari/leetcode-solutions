# Brute Force approach using space
# time complexity O(n*m)
# Space complexity O(n)
class Solution:
    def mostVisited(self, n: int, rounds) :
        count = [0]*n
        for i in range(len(rounds)-1):
            a =rounds[i]
            b = rounds[i+1]
            while a!=b:
                print(a)
                count[a-1]+=1
                a = (a%n)+1
        count[rounds[i+1]-1]+=1
        
        maxi = max(count)
        ans = []
        for i in range(len(count)):
            if maxi==count[i]:
                ans.append(i+1)
        return ans

# approach 2 using simulation of circle
# time compelxity O(n)
# space comlexity O(1)

class Solution:
    def mostVisited(self, n: int, rounds):
     start, end = rounds[0], rounds[-1]
     if start <= end:
            return list(range(start, end+1))
     else:
            return list(range(1, end+1)) + list(range(start, n+1))