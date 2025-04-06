from collections import defaultdict
from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        distincts = defaultdict(int)
        visited = set()

        for i, s in enumerate(arr):
            if s in distincts:
                distincts.pop(s)
                visited.add(s)
            elif s not in visited:
                distincts[s] += i

        result = sorted(distincts, key=distincts.get)
        return result[k - 1] if len(result) >= k else ""
