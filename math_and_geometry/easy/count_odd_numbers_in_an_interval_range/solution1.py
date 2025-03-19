class Solution:
    def countOdds(self, low: int, high: int) -> int:
        length = high - low + 1
        count = length // 2

        if low % 2 and high % 2:
            count += 1

        return count
