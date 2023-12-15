class Solution:
    def leastBricks(self, wall: list[list[int]]) -> int:
        countGap = {0: 0} # - Mapping position to count of brick gaps

        for row_of_bricks in wall:
            total = 0
            for brick in row_of_bricks[:-1]:
                total += brick
                countGap[total] = 1 + countGap.get(total, 0)
        
        return len(wall) - max(countGap.values())
        