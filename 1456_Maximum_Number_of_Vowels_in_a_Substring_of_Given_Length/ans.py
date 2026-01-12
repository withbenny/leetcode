class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        current = sum(1 for ch in s[:k] if ch in vowels)
        max_vowels = current

        for i in range(k, len(s)):
            if s[i] in vowels:
                current += 1
            if s[i - k] in vowels:
                current -= 1
            max_vowels = max(max_vowels, current)

        return max_vowels

if __name__ == "__main__":
    sol = Solution()
    s = "weallloveyou"
    k = 7
    print(sol.maxVowels(s, k))