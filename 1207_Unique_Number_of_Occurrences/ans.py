from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        for a in arr:
            freq[a] = freq.get(a, 0) + 1
        
        return len(freq) == len(set(freq.values()))

if __name__ == "__main__":
    sol = Solution()
    arr = [1,2,2,1,1,3]
    print(sol.uniqueOccurrences(arr))