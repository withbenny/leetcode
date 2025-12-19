class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""

        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    candidate = s[i : j + 1]
                    if candidate == candidate[:: -1]:
                        if len(candidate) > len(longest):
                            longest = candidate
        
        return longest

if __name__ == "__main__":
    sol = Solution()
    s = "babad"
    print(sol.longestPalindrome(s))