from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
    	if not strs:
    		return ""

    	return self._divide_and_conquer(strs, 0, len(strs) - 1)

    def _divide_and_conquer(self, strs: List[str], left: int, right: int) -> str:
    	if left == right:
    		return strs[left]

    	mid = (left + right) // 2
    	lcp_left = self._divide_and_conquer(strs, left, mid)
    	lcp_right = self._divide_and_conquer(strs, mid + 1, right)

    	return self._merge(lcp_left, lcp_right)

    def _merge(self, left_str: str, right_str: str) -> str:
    	min_len = min(len(left_str), len(right_str))

    	for i in range(min_len):
    		if left_str[i] != right_str[i]:
    			return	left_str[:i]

    	return left_str[:min_len]


if __name__ == "__main__":
    sol = Solution()
    strs = ["flower","flow","flight"]
    print(sol.longestCommonPrefix(strs))