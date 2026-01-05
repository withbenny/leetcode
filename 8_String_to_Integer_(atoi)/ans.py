class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0

        INT_MAX = pow(2, 31) - 1
        INT_MIN = -pow(2, 31)

        i = 0
        n = len(s)

        while i < n and s[i] == " ":
            i += 1

        if i == n:
            return 0

        sign = 1
        if s[i] == "-":
            sign = -1
            i += 1
        elif s[i] == "+":
            i += 1

        out = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            out = out * 10 + digit
            i += 1

            if sign * out <= INT_MIN:
                return INT_MIN
            elif sign * out >= INT_MAX:
                return INT_MAX

        return sign * out


if __name__ == '__main__':
    sol = Solution()
    s = "   -042"
    print(sol.myAtoi(s))