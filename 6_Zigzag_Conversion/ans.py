class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        n = len(s)
        cycle_len = 2 * numRows - 2
        numCol = (n // cycle_len + 1) * (numRows - 1)

        a = [["" for _ in range(numCol)] for _ in range(numRows)]
        r, c = 0, 0
        d_down = True
        for char in s:
            a[r][c] = char

            if d_down:
                if r == numRows - 1:
                    d_down = False
                    r -= 1
                    c += 1
                else:
                    r += 1
                    c += 0
            else:
                if r == 0:
                    r += 1
                    c += 0
                    d_down = True
                else:
                    r -= 1
                    c += 1
        
        result = ""
        for row in a:
            row_str = "".join(row)
            result += row_str
        
        return result

if __name__ == '__main__':
    sol = Solution()
    s = "PAYPALISHIRING"
    numRows = 3
    print(sol.convert(s, numRows))