from collections import defaultdict
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # hashmap: store all bits frequency
        # go through all number which is the power of 2
        def findNumberFreq(x):
            freq_map = defaultdict(int)
            while x > 0:
                freq_map[x % 10] += 1
                x //= 10
            return freq_map

        n_freq = findNumberFreq(n)

        for i in range(32):
            power_of_two = 2 ** i
            if findNumberFreq(power_of_two) == n_freq:
                return True
        return False

