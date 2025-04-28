from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        current = odd = even = 0
        result = 0
        MOD = (10 ** 9 + 7)

        for num in arr:
            current += num
            if current % 2:  # odd sum
                result += (1 + even) % MOD
                odd += 1
            else:  # even sum
                result += (odd) % MOD
                even += 1

        return result % MOD
