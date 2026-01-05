class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
        elif x == 0:
            return 0
        else:
            sign = 1
        
        out = 0
        num = abs(x)
        while num != 0:
            digit = num % 10
            num //= 10
            out = out * 10 + digit
        
        out *= sign
        if out < -pow(2, 31) or out > pow(2, 31) - 1:
            return 0
        
        return out

if __name__ == '__main__':
    sol = Solution()
    x = -123
    print(sol.reverse(x))