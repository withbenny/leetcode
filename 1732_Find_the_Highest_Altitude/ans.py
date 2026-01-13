from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [0]
        for i in range(0, len(gain)):
            altitudes.append(altitudes[i] + gain[i])
        
        return max(altitudes)

if __name__ == "__main__":
    sol = Solution()
    gain = [-5,1,5,0,-7]
    print(sol.largestAltitude(gain))