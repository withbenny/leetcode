from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        s = ""
        result = []

        def _dfs(left, right, s):
            if len(s) == n * 2:
                result.append(s)
                return

            if left < n:
                _dfs(left + 1, right, s + "(")
            if right < left:
                _dfs(left, right + 1, s + ")")

        _dfs(0, 0, s)
        return result

if __name__ == "__main__":
    sol = Solution()
    n = 3
    print(sol.generateParenthesis(n))