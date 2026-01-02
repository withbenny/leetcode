from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            w = right - left
            h = min(height[left], height[right])
            max_area  = max(max_area, w * h)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

if __name__ == "__main__":
    sol = Solution()
    height = [4,3,2,1,4]
    print(sol.maxArea(height))