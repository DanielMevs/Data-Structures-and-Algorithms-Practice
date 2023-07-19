class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for letter in ransomNote:
            if letter in magazine:
                magazine = magazine[:magazine.index(letter)] + magazine[magazine.index(letter) + 1:]
            else:
                return False
        return True