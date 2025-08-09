class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # DP
        i = j = k = 0
        num_arr = [1]
        for _ in range(n - 1):
            min_num = min(num_arr[i] * 2, num_arr[j] * 3, num_arr[k] * 5)
            num_arr.append(min_num)
            if min_num == num_arr[i] * 2:
                i += 1
            if min_num == num_arr[j] * 3:
                j += 1
            if min_num == num_arr[k] * 5:
                k += 1
        return num_arr[-1]