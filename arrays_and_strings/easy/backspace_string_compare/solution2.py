class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def nextValidCharIndex(st: str, index: int) -> int:
            backspaceCount = 0
            while index >= 0:
                if st[index] == '#':
                    backspaceCount += 1
                elif backspaceCount > 0:
                    backspaceCount -= 1
                else:
                    break
                index -= 1

            return index
        
        sTracker, tTracker = len(s) - 1, len(t) - 1
        while sTracker >= 0 or tTracker >= 0:
            sTracker = nextValidCharIndex(s, sTracker)
            tTracker = nextValidCharIndex(t, tTracker)
            if sTracker < 0 and tTracker < 0:
                return True
            if sTracker < 0 or tTracker < 0:
                return False
            if s[sTracker] != t[tTracker]:
                return False
            sTracker, tTracker = sTracker - 1, tTracker - 1
        
        return True
    