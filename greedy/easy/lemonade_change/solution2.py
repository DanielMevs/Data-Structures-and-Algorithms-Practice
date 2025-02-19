from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five == 0:
                    return False
                ten, five = ten + 1, five - 1
            # bill == 20
            else:
                if ten > 0 and five > 0:
                    ten, five = ten - 1, five - 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True
