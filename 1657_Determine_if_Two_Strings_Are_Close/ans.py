class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        cnt1 = Counter(word1)
        cnt2 = Counter(word2)

        return (cnt1.keys() == cnt2.keys() and sorted(cnt1.values()) == sorted(cnt2.values()))

if __name__ == "__main__":
    sol = Solution()
    # word1 = "abc"
    # word2 = "bca"
    word1 = "a"
    word2 = "aa"
    print(sol.closeStrings(word1, word2))