class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sArr1, sArr2 = [], []
        for char in s:
            if sArr1 and char == '#':
                sArr1.pop()
            elif char != '#':
                sArr1.append(char)
        
        for char in t:
            if sArr2 and char == '#':
                sArr2.pop()
            elif char != '#':
                sArr2.append(char)

        return sArr1 == sArr2
    