from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        left, right = 1, 1
        for i in range(n):
            result[i] *= left
            left *= nums[i]
            result[n - i - 1] *= right
            right *= nums[n - i - 1]

        return result

if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3,4]
    print(sol.productExceptSelf(nums))