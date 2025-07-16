class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # 1. even -> even -> even
        # 2. odd -> odd -> odd
        # 3. odd -> even -> odd (cross)
        even = 0
        for num in nums:
            if num % 2 == 0:
                even += 1
        cross = 0
        state = ""
        for num in nums:
            if num % 2 == 0 and state != "even":
                cross += 1
                state = "even"
            elif num % 2 == 1 and state != "odd":
                cross += 1
                state = "odd"
        return max(even, len(nums) - even, cross)


        # dp = [[0 for _ in range(len(nums))] for _ in range(2)]
        # for i in range(1, len(nums)):
        #     if (nums[i] + nums[i - 1]) % 2 == 0:
        #         dp[0][i] = dp[0][i - 1] + 1
        #         dp[1][i] = dp[1][i - 1]
        #     else:
        #         dp[0][i] = dp[0][i - 1]
        #         dp[1][i] = dp[1][i - 1] + 1
        # print(dp)
        # return max(dp[0][-1], dp[1][-1]) + 1