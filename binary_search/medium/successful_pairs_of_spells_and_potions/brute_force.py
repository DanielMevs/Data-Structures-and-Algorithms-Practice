# - O(n*m) runtime; n=|spells| and m=|potions|

class Solution:
    def successfulPairs(
            self, spells: list[int], potions: list[int],
            success: int) -> list[int]:
        output = []
        for spell in spells:
            count = 0
            for potion in potions:
                if spell * potion >= success:
                    count += 1
            output.append(count)
        
        return output