class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x >=0 and x < 10:
            return True
        
        s = str(x)
        reversed_s = s[::-1]
        if reversed_s == s:
            return True
        else:
            return False

if __name__ == "__main__":
    sol = Solution()
    x = 121
    print(sol.isPalindrome(x))