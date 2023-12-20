class Solution:
    def gridGame(self, grid: list[list[int]]) -> int:
        num_of_cols = len(grid[0])
        prefix_sum1, prefix_sum2 = grid[0].copy(), grid[1].copy()

        for i in range(1, num_of_cols):
            prefix_sum1[i] += prefix_sum1[i - 1]
            prefix_sum2[i] += prefix_sum2[i - 1]
        
        result = float("inf")

        for i in range(num_of_cols):
            top = prefix_sum1[-1] - prefix_sum1[i]
            bottom = prefix_sum2[i - 1] if i > 0 else 0
            secondRobot = max(top, bottom)
            result = min(result, secondRobot)
        
        return result
