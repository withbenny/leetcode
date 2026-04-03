class Solution:
    def removeStars(self, s: str) -> str:
        result = []
        for ch in s:
            if ch == "*":
                result.pop()
            else:
                result.append(ch)

        return "".join(result)


if __name__ == "__main__":
    sol = Solution()
    s = "leet**cod*e"
    print(sol.removeStars(s))
