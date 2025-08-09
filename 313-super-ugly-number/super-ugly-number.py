class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ptrs = [0] * len(primes)
        uglyArr = [1]
        for _ in range(n - 1):
            minUgly = float(inf)
            for i in range(len(ptrs)):
                minUgly = min(minUgly, uglyArr[ptrs[i]] * primes[i])
            uglyArr.append(minUgly)
            for i in range(len(ptrs)):
                if minUgly == uglyArr[ptrs[i]] * primes[i]:
                    ptrs[i] += 1
        return uglyArr[-1]