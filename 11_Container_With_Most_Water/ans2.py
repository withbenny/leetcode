from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            left_h = height[left]
            right_h = height[right]

            if left_h < right_h:
                max_area = max(max_area, left_h * (right - left))
                while left < right and height[left] <= left_h:
                    left += 1
            else:
                max_area = max(max_area, right_h * (right - left))
                while left < right and height[right] <= right_h:
                    right -= 1

        return max_area

if __name__ == "__main__":
    sol = Solution()
    height = [4,3,2,1,4]
    print(sol.maxArea(height))