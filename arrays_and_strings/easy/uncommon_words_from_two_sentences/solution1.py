from collections import defaultdict
from typing import List


class Solution:
    def uncommonFromSentences(
            self, s1: str, s2: str) -> List[str]:
        count = defaultdict(int)

        for word in s1.split() + s2.split():
            count[word] += 1

        return [word for word in count if count[word] == 1]
