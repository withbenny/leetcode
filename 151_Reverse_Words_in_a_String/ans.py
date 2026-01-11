class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])

if __name__ == "__main__":
    sol = Solution()
    s = "the sky is blue"
    print(sol.reverseWords(s))