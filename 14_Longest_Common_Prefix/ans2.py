from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        min_len = min(len(s) for s in strs)
        low, high = 1, min_len

        while low <= high:
            mid = (low + high) // 2

            if self._isCommon(strs, mid):
                low = mid + 1
            else:
                high = mid - 1

        return strs[0][:high]

    def _isCommon(self, strs: List[str], length: int) -> bool:
        prefix = strs[0][:length]

        for i in range(1, len(strs)):
            if not strs[i].startswith(prefix):
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    strs = ["flower", "flow", "flight"]
    print(sol.longestCommonPrefix(strs))
