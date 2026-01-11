class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        s = list(s)
        
        ind = []
        v = []
        for i, j in enumerate(s):
            if j in vowels:
                ind.append(i)
                v.append(j)

        v = v[::-1]

        for m, n in zip(ind, v):
            s[m] = n

        return "".join(s)

if __name__ == "__main__":
    sol = Solution()
    s = "IceCreAm"
    print(sol.reverseVowels(s))