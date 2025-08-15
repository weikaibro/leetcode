class Solution:
    def numTrees(self, n: int) -> int:
        # 3 node: 1 root + 2 right / 1 root + 1 left + 1 right / 1 root + 2 left
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[-1]