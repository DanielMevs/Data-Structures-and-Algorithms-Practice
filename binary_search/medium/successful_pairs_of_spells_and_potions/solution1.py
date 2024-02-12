# - O(nlogm + mlogm) runtime; n=|spells| and m=|potions|

class Solution:
    def successfulPairs(
            self, spells: list[int], potions: list[int],
            success: int) -> list[int]:
        potions.sort()
        result = []

        for spell in spells:
            left, right = 0, len(potions) - 1
            # - Find the weakest potion (furthest
            #   to the left) that works
            idx = len(potions)

            while left <= right:
                
                mid = (left + right) // 2
                if spell * potions[mid] >= success:
                    right = mid - 1
                    idx = mid
                else:
                    left = mid + 1
            
            result.append(len(potions) - idx)

        return result