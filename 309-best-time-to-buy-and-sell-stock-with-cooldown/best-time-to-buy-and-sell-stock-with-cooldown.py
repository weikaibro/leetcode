class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0 for _ in range(len(prices))] for _ in range(3)]
        # state: 0 - hold / 1 - sell / 2 - cooldown
        # 0 -> 1 -> 2 -> 0 -> ...
        dp[0][0], dp[1][0], dp[2][0] = -prices[0], 0, 0
        for day in range(1, len(prices)):
            dp[0][day] = max(dp[0][day - 1], dp[2][day - 1] - prices[day])
            dp[1][day] = dp[0][day - 1] + prices[day]
            dp[2][day] = max(dp[1][day - 1], dp[2][day - 1])
        return max(dp[1][-1], dp[2][-1])

