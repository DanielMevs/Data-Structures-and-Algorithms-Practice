class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        for letter in s:
            if i < len(t) and letter == t[i]:
                i += 1

        return len(t) - i
