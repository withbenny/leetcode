from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1, set2 = set(nums1), set(nums2)
        return [list(set1 - set2), list(set2 - set1)]

if __name__ == "__main__":
    sol = Solution()
    nums1 = [1,2,3,3]
    nums2 = [1,1,2,2]
    print(sol.findDifference(nums1, nums2))