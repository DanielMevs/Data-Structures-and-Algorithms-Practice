from typing import List


class Solution:
    # O(N^2) time, O(1) space
    def minFallingPathSum(self, grid: List[List[int]]) -> int:

        def get_min_two(row):
            two_smallest = []  # (val, idx)
            for val, idx in row:
                if len(two_smallest) < 2:
                    two_smallest.append((val, idx))
                elif two_smallest[1][0] > val:
                    two_smallest.pop()
                    two_smallest.append((val, idx))
                two_smallest.sort()
            return two_smallest

        N = len(grid)
        first_row = [(val, idx) for idx, val in enumerate(grid[0])]
        dp = get_min_two(first_row)

        for r in range(1, N):
            next_dp = []  # (val, idx)
            for curr_c in range(N):
                curr_val = grid[r][curr_c]
                min_val = float('inf')
                for prev_val, prev_c in dp:
                    if prev_c != curr_c:
                        min_val = min(min_val, curr_val + prev_val)
                next_dp.append((min_val, curr_c))
                next_dp = get_min_two(next_dp)
            dp = next_dp

        return min(val for val, _ in dp)
