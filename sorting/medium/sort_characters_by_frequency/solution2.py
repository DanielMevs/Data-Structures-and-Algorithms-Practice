from collections import Counter, defaultdict


class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)  # char -> freq
        buckets = defaultdict(list)  # freq -> [char]

        for char, cnt in count.items():
            buckets[cnt].append(char)

        result = []
        for i in range(len(s), 0, -1):
            for c in buckets[i]:
                result.append(c * i)
        
        return ''.join(result)
