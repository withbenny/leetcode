class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        total = 0
        n = len(s)
        for i in range(n):
            value = roman_map[s[i]]

            if i < n - 1 and value < roman_map[s[i + 1]]:
                total -= value
            else:
                total += value

        return total

if __name__ == "__main__":
    sol = Solution()
    s = 'MCMXCIV'
    print(sol.romanToInt(s))