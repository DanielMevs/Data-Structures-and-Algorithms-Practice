from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        result = 0
        left, right = 0, 0

        while right < len(s):
            count[s[right]] += 1
            # - Most frequent character
            maxCount = max(count.values())

            # - Size of the window
            subStrLen = right - left + 1
            # - Number of characters to replace
            replaceNum = subStrLen - maxCount
            if replaceNum <= k:
                result = max(result, subStrLen)
                right += 1
            else:
                count[s[left]] -= 1
                count[s[right]] -= 1
                left += 1
        
        return result
        
