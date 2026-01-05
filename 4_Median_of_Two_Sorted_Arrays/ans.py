from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = nums1 + nums2
        num = sorted(num)
        length = len(num)
        
        if length % 2 == 0:
            return (num[length // 2 - 1] + num[length // 2]) /2 
        else:
            return num[length // 2]

if __name__ == '__main__':
    sol = Solution()
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(sol.findMedianSortedArrays(nums1, nums2))