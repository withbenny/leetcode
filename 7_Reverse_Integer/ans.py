class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            out = -int(str(-x)[::-1])
        else:
            out = int(str(x)[::-1])
        
        if out < -pow(2, 31) or out > pow(2, 31) - 1:
            return 0
        
        return out

if __name__ == '__main__':
    sol = Solution()
    x = -123
    print(sol.reverse(x))