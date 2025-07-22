class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        maxSum = 0
        num_set = set()

        left = 0
        for right in range(len(nums)):
            if nums[right] not in num_set:
                num_set.add(nums[right])
            else:
                maxSum = max(maxSum, sum(nums[left:right]))
                while True:
                    if nums[left] == nums[right]:
                        left += 1
                        break
                    num_set.remove(nums[left])
                    left += 1
        return max(maxSum, sum(nums[left:]))

            
