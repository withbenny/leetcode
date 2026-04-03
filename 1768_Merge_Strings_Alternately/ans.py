class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []

        for a, b in zip(word1, word2):
            result.append(a + b)

        result.append(word1[len(word2) :])
        result.append(word2[len(word1) :])

        return "".join(result)


if __name__ == "__main__":
    sol = Solution()
    word1 = "ac"
    word2 = "pqrd"
    print(sol.mergeAlternately(word1, word2))
