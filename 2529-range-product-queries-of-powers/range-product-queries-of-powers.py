class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # bit manipulation: find power of 2 element
        # query
        MOD = 10 ** 9 + 7

        binarys = bin(n)[2:]
        bases = []
        for i in range(len(binarys)):
            if binarys[-1 - i] == "1":
                bases.append(int(binarys[-1 - i], 2) * 2 ** i)
        # print(bases)
        result = []
        for query in queries:
            start, end = query[0], query[1]
            multiples = bases[start]
            for i in range(start + 1, end + 1):
                multiples = (multiples * bases[i]) % MOD
            result.append(multiples)
        return result
        