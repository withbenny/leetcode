from typing import List
from collections import Counter

import numpy as np


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_counts = Counter(tuple(row) for row in grid)
        t_grid = list(map(list, zip(*grid)))
        count = 0

        for col in t_grid:
            col_tuple = tuple(col)
            if col_tuple in row_counts:
                count += row_counts[col_tuple]

        return count


if __name__ == "__main__":
    sol = Solution()
    grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
    print(sol.equalPairs(grid))
