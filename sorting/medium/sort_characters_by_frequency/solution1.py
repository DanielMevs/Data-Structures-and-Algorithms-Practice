from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        temp = ''.join(sorted(count.keys(), key=count.get, reverse=True))
        result = ''
        for char in temp:
            result += char * count[char]
        return result
        