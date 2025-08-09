from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # sliding window 
        # hashmap -> store the count of each fruit type
        type_count_map = defaultdict(int)
        left = 0
        max_length = 0
        for right in range(len(fruits)):
            type_count_map[fruits[right]] += 1
            while len(type_count_map) >= 3:
                type_count_map[fruits[left]] -= 1
                if type_count_map[fruits[left]] <= 0:
                    del type_count_map[fruits[left]]
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length
