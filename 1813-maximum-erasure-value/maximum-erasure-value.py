class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        maxSum, currSum = 0, 0
        num_set = set()

        left = 0
        for right in range(len(nums)):
            if nums[right] not in num_set:
                num_set.add(nums[right])
                currSum += nums[right]
            else:
                while True:
                    if nums[left] == nums[right]:
                        left += 1
                        break
                    num_set.remove(nums[left])
                    currSum -= nums[left]
                    left += 1
            maxSum = max(maxSum, currSum)
        return maxSum

            
