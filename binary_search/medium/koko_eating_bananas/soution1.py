import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)
        min_k = right

        while left <= right:
            k = left + ((right - left) // 2)

            hours_count = 0

            for pile in piles:
                hours_count += math.ceil(pile / k)


            if hours_count <= h:
                min_k = min(min_k, k)
                right = k - 1

            else:
                left = k + 1

        return min_k
            