# approach used here is monotonic stack to find the next smallest element
# time complexity O(n)
# space complexity O(n)
class Solution:
    def finalPrices(self, prices):
        n = len(prices)
        result = [-1]*n
        stack = []
        for i in range(n):
            while stack and prices[i]<=prices[stack[-1]]:
                result[stack.pop()] = prices[i]
            stack.append(i)
    
        for i in range(n):
            if result[i]!=-1:
                prices[i] = prices[i]-result[i]
        return prices