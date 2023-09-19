class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        max_pile = max(piles)
        # potential_k_list = [i for i in range(1, max_pile)]
        left, right = 1, max_pile
        min_k = float("inf")
        while left <= right:
            mid = left + ((right - left) // 2)
            count = 0
            for pile in piles:
                count += (pile / mid)
            if count < h:
                min_k = min(min_k, count)
                right = mid - 1
            elif count > h:
                left = mid + 1
        return min_k
            