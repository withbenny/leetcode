from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mappings = {
            '2': "abc", '3': "edf",
            '4': "ghi", '5': "jkl", '6': "mno",
            '7': "pqrs", '8': "tuv", '9': "wxyz",
        }

        result = []

        def _backtrace(index: int, current_str: str):
            if len(current_str) == len(digits):
                result.append(current_str)
                return
            
            current_digit = digits[index]
            for char in mappings[current_digit]:
                _backtrace(index + 1, current_str + char)

        _backtrace(0, "")

        return result
        
if __name__ == "__main__":
    sol = Solution()
    digits = "23"
    print(sol.letterCombinations(digits))