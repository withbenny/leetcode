from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        read = 0
        n = len(chars)

        while read < n:
            c = chars[read]
            count = 0
            while read < n and chars[read] == c:
                read += 1
                count += 1

            chars[write] = c
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write


if __name__ == "__main__":
    sol = Solution()
    chars = ["a", "a", "b", "b", "c", "c", "c"]
    print(sol.compress(chars))
