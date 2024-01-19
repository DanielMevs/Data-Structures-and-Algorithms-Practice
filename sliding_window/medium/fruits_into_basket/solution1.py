from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        # - Mapping fruit type to the count of the fruit
        count = defaultdict(int)
        left, total, result = 0, 0, 0
        for right in range(len(fruits)):
            count[fruits[right]] += 1
            total += 1
            while len(count) > 2:
                fruit = fruits[left]
                count[fruit] -= 1
                total -= 1
                left += 1

                if not count[fruit]:
                    count.pop(fruit)

            result = max(result, total)
            
        return result

        