class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        result = 0

        while left <= right:
            mid = (left + right) // 2
            coins = (mid / 2) * (mid + 1)
            if coins > n:
                right = mid - 1
            else:
                left = mid + 1
                result = max(mid, result)

        return result
    