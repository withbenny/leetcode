from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        result = []
        for n in candies:
            if n + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)

        return result

if __name__ == "__main__":
    sol = Solution()
    candies = [2,3,5,1,3]
    extraCandies = 3
    print(sol.kidsWithCandies(candies, extraCandies))