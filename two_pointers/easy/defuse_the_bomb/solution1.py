from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        result = []
        n = len(code)

        for i in range(n):
            current_sum = 0
            if k > 0:
                for j in range(i + 1, i + k + 1):
                    idx = j % n
                    current_sum += code[idx]
            elif k < 0:
                for j in range(i - 1, i + k - 1, -1):
                    idx = j % n
                    current_sum += code[idx]

            result.append(current_sum)

        return result
