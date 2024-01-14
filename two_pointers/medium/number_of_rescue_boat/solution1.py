class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()

        # - Boats
        result = 0

        left, right = 0, len(people)  - 1
        while left <= right:
            remaining = limit - people[right]
            right -= 1
            result += 1
            if left <= right and remaining >= people[left]:
                left += 1
        
        return result