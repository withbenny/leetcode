class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        n = [""] * numRows
        current = 0
        step = 1
        for char in s:
            n[current] += char

            if current == 0:
                step = 1
            elif current == numRows - 1:
                step = -1
            current += step
        
        return "".join(n)

if __name__ == '__main__':
    sol = Solution()
    s = "PAYPALISHIRING"
    numRows = 3
    print(sol.convert(s, numRows))