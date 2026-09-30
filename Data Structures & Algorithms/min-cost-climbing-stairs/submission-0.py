class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [None] * len(cost)

        dp[0] = 0
        dp[1] = 0

        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1])
        print(dp)
        return min(dp[-1] + cost[-1], cost[-2] + dp[-2])