from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        result = 0
        maxFreq = 0
        left, right = 0, 0

        while right < len(s):
            count[s[right]] += 1
            # - Most frequent character
            maxFreq = max(count[s[right]], maxFreq)

            # - Size of the window
            subStrLen = right - left + 1
            # - Number of characters to replace
            replaceNum = subStrLen - maxFreq
            while replaceNum > k:
                count[s[left]] -= 1
                left += 1
                subStrLen = right - left + 1
                replaceNum = subStrLen - maxFreq
            result = max(result, subStrLen)
            right += 1
        
        return result
        
