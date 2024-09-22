from collections import defaultdict
from typing import List


class Solution:
    def numSubmatrixSumTarget(
            self, matrix: List[List[int]], target: int) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        sub_sum = [[0] * (COLS) for _ in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):
                top = sub_sum[r - 1][c] if r > 0 else 0
                left = sub_sum[r][c - 1] if c > 0 else 0
                top_left = sub_sum[r - 1][c - 1] if min(r, c) > 0 else 0
                sub_sum[r][c] = matrix[r][c] + top + left - top_left
        
        result = 0
        
        for r1 in range(ROWS):
            for r2 in range(r1, ROWS):
                count = defaultdict(int)  # prefix sum -> count
                count[0] = 1
                for c in range(COLS):
                    current_sum = sub_sum[r2][c] - (sub_sum[r1 - 1][c] if r1 > 0 else 0)
                    diff = current_sum - target
                    result += count[diff]
                    count[current_sum] += 1
        
        return result
                
