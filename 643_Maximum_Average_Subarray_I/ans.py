from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current = max_sum = sum(nums[:k])
        for i in range(k, len(nums)):
            current += nums[i] - nums[i - k]
            max_sum = max(current, max_sum)

        return max_sum / k


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    print(sol.findMaxAverage(nums, k))
