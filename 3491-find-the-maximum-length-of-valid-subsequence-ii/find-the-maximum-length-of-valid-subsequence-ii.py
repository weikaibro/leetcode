class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        max_length = 2
        for i in range(k):
            dp = [0] * k
            for num in nums:
                remainder = num % k
                require = (i - remainder) % k
                dp[remainder] = dp[require] + 1
            max_length = max(max_length, max(dp))
        return max_length
                