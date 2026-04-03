class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        c_num = 0
        c_str = ""

        for char in s:
            if char.isdigit():
                c_num = c_num * 10 + int(char)
            elif char == "[":
                stack.append((c_str, c_num))
                c_num = 0
                c_str = ""
            elif char == "]":
                p_str, repeat = stack.pop()
                c_str = p_str + c_str * repeat
            else:
                c_str += char

        return c_str


if __name__ == "__main__":
    sol = Solution()
    s = "3[a]2[bc]"
    print(sol.decodeString(s))
