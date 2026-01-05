class Solution:
    def intToRoman(self, num: int) -> str:
        roman_symbols = {
            3000: 'MMM', 2000: 'MM', 1000: 'M', 900: 'CM', 800: 'DCCC',
            700: 'DCC', 600: 'DC', 500: 'D', 400: 'CD', 300: 'CCC',
            200: 'CC', 100: 'C', 90: 'XC', 80: 'LXXX', 70: 'LXX',
            60: 'LX', 50: 'L', 40: 'XL', 30: 'XXX', 20: 'XX',
            10: 'X', 9: 'IX', 8: 'VIII', 7: 'VII', 6: 'VI',
            5: 'V', 4: 'IV', 3: 'III', 2: 'II', 1: 'I', 0: ''
        }

        num_4 = num - (num % 1000)
        num_3 = (num % 1000) - (num % 100)
        num_2 = (num % 100) - (num % 10)
        num_1 = num % 10

        roman = roman_symbols[num_4] + roman_symbols[num_3] + roman_symbols[num_2] + roman_symbols[num_1]
        return roman

if __name__ == "__main__":
    sol = Solution()
    num = 3749
    print(sol.intToRoman(num))