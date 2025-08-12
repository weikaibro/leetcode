# class Solution:
#     def numberOfWays(self, n: int, x: int) -> int:
#         # dfs: if exceeds n, backtracks another path
#         bases = []
#         for i in range(1, n + 2):
#             if i ** x > n:
#                 break
#             else:
#                 bases.append(i ** x)
#         @lru_cache(maxsize=10**6)
#         def backtracking(remaining, idx):
#             if remaining == 0:
#                 return 1
#             if remaining < 0 or idx == len(bases):
#                 return 0
            
#             include = backtracking(remaining - bases[idx], idx + 1)
#             exclude = backtracking(remaining, idx + 1)
#             return (include + exclude) % (10 ** 9 + 7)
        
#         return backtracking(n, 0)
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        from functools import lru_cache
        MOD = 10**9 + 7

        @lru_cache(None)
        def dp(remaining, current):
            if remaining == 0:
                return 1
            if remaining < 0 or current ** x > remaining:
                return 0

            power = current ** x
            # Try including current or skipping it
            include = dp(remaining - power, current + 1)
            skip = dp(remaining, current + 1)
            return (include + skip) % MOD

        return dp(n, 1)