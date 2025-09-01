from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_ransom, count_magazine = Counter(ransomNote), Counter(magazine)
        for letter, count in count_magazine.items():
            if count_ransom[letter] > count:
                return False
            del count_ransom[letter]
        return True if not count_ransom else False
