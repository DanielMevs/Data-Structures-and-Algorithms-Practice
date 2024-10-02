from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        result = score = 0
        tokens.sort()

        left, right = 0, len(tokens) - 1

        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                left += 1
                score += 1
                result = max(result, score)
            elif score > 0:
                power += tokens[right]
                right -= 1
                score -= 1
            else:
                break
        
        return result