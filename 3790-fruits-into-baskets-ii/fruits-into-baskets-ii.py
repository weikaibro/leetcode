class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        result = 0
        for fruit in fruits:
            idx = 0
            while idx <= len(baskets):
                if idx == len(baskets):
                    result += 1
                    break
                if fruit <= baskets[idx]:
                    baskets.pop(idx)
                    break
                else:
                    idx += 1
        return result