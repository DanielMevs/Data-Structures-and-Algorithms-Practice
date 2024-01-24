class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '':
            return ''
        
        countT, window = {}, {}

        for char in t:
            countT[char] = countT.get(char, 0) + 1
        
        have, need = 0, len(countT)
        result, resultLen = [-1, -1], float('inf')
        left = 0

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1
            if char in countT and window[char] == countT[char]:
                have += 1
            while have == need:
                # - Update our result
                if (right - left + 1) < resultLen:
                    result = [left, right]
                    resultLen = (right - left + 1)
                # - Pop from the left of our window
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1

                
        left, right = result

        return s[left: right + 1] if resultLen != float('inf') else ''
                    

