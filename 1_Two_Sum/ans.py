from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        
        for i in range(n):
            for j in range(i+1, n):
                num1 = nums[i]
                num2 = nums[j]
                sum = num1 + num2
                if sum == target:
                    return [i, j]
        return []

if __name__ == "__main__":
    sol = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(sol.twoSum(nums, target))