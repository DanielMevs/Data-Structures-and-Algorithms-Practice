class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        seen, result = set(), set()

        for left in range(len(s) - 9):
            current = s[left: left + 10]
            if current in seen:
                result.add(current)
            
            seen.add(current)
        
        return list(result)