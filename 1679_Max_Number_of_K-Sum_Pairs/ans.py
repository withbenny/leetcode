from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        count = 0

        while left < right:
            total = nums[left] + nums[right]
            if total == k:
                count += 1
                left += 1
                right -= 1
            elif total > k:
                right -= 1
            else:
                left += 1

        return count


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 4]
    k = 5
    print(sol.maxOperations(nums, k))
