from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        result = nums[0] + nums[1] + nums[2]
        
        for i in range(n):
            j = i + 1
            k = n - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                
                if abs(target - total) < abs(target - result):
                    result = total
                
                if total == target:
                    return target
                elif total < target:
                    j += 1
                else:
                    k -= 1
        
        return result  
            
if __name__ == "__main__":
    sol = Solution()
    nums = [-1,2,1,-4]
    target = 1
    print(sol.threeSumClosest(nums, target))