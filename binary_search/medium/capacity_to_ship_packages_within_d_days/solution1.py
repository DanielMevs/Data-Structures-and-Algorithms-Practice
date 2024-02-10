class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        result = right

        def canShip(capacity):
            ships, currentCap = 1, capacity
            for weight in weights:
                if currentCap - weight < 0:
                    ships += 1
                    currentCap = capacity
                currentCap -= weight
            return ships <= days

        while left <= right:
            capacity = (left + right) // 2
            if canShip(capacity):
                result = min(result, capacity)
                right = capacity - 1
            else:
                left = capacity + 1
        
        return result