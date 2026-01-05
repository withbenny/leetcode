class Solution:
    def romanToInt(self, s: str) -> int:    
        roman_symbols = {
            3000: 'MMM', 2000: 'MM', 1000: 'M', 900: 'CM', 800: 'DCCC',
            700: 'DCC', 600: 'DC', 500: 'D', 400: 'CD', 300: 'CCC',
            200: 'CC', 100: 'C', 90: 'XC', 80: 'LXXX', 70: 'LXX',
            60: 'LX', 50: 'L', 40: 'XL', 30: 'XXX', 20: 'XX',
            10: 'X', 9: 'IX', 8: 'VIII', 7: 'VII', 6: 'VI',
            5: 'V', 4: 'IV', 3: 'III', 2: 'II', 1: 'I', 0: ''
        }

        result = 0
        for value, symbol in roman_symbols.items():
            if s.startswith(symbol):
                result += value
                s = s[len(symbol):]

        return result

if __name__ == "__main__":
    sol = Solution()
    s = 'MCMXCIV'
    print(sol.romanToInt(s))