from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        count = Counter(s)
        used_freq = set()
        result = 0  # number of deletions

        for c, freq in count.items():
            while freq > 0 and freq in used_freq:
                freq -= 1
                result += 1
            used_freq.add(freq)  # freq = either unique or 0

        return result
