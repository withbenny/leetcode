from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        j = 0
        n = len(asteroids)

        for i in range(n):
            a = asteroids[i]
            while j > 0 and asteroids[j - 1] > 0 and a < 0 and asteroids[j - 1] < abs(a):
                j -= 1

            if j == 0 or a > 0 or asteroids[j - 1] < 0:
                asteroids[j] = a
                j += 1
            elif asteroids[j - 1] == abs(a):
                j -= 1

        return asteroids[:j]

if __name__ == "__main__":
    sol = Solution()
    asteroids = [5,10,-5]
    print(sol.asteroidCollision(asteroids))