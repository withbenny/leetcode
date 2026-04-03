from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        minLeft = [0] * n
        minLeft[0] = nums[0]
        for i in range(1, n):
            minLeft[i] = min(minLeft[i - 1], nums[i])

        maxRight = nums[-1]
        for i in range(n - 2, 0, -1):
            if minLeft[i] < nums[i] < maxRight:
                return True
            maxRight = max(maxRight, nums[i])

        return False


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 1, 5, 0, 4, 6]
    print(sol.increasingTriplet(nums))
