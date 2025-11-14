# approach is used here is dynamic programming
# time complexity O(n)
# space complexity O(n)
class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        n = len(cost)
        dp =[cost[i] for i in range(n)]
        dp.append(0) 
        for i in range(n-2,-1,-1):
            dp[i] = cost[i]+min(dp[i+1],dp[i+2])
        return min(dp[0],dp[1])

