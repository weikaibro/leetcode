class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        # delete the larger number in the left, the smaller number in the right
        n3 = len(nums)
        n = n3 // 3

        leftMinSum = [0] * n3
        rightMinSum = [0] * n3

        maxHeap = []
        leftCurrSum = 0
        for i in range(n3):
            heapq.heappush(maxHeap, -nums[i])
            leftCurrSum += nums[i]
            if len(maxHeap) >= n + 1:
                leftCurrSum += heapq.heappop(maxHeap)
            if i >= n - 1:
                leftMinSum[i] = leftCurrSum
        
        minHeap = []
        rightCurrSum = 0
        for i in range(n3 - 1, -1, -1):
            heapq.heappush(minHeap, nums[i])
            rightCurrSum += nums[i]
            if len(minHeap) >= n + 1:
                rightCurrSum -= heapq.heappop(minHeap)
            if i <= n3 - n:
                rightMinSum[i] = rightCurrSum

        result = float('inf')
        for i in range(n - 1, n3 - n):
            result = min(result, leftMinSum[i] - rightMinSum[i + 1])

        return result