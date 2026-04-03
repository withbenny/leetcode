from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0

        for i in range(len(nums)):
            right = total - left - nums[i]

            if right == left:
                return i

            left += nums[i]

        return -1


if __name__ == "__main__":
    sol = Solution()
    # nums = [1,7,3,6,5,6]
    nums = [0, 0]
    print(sol.pivotIndex(nums))
