from collections import Counter
from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)

        result = [s for s in arr if count[s] == 1]
        return result[k - 1] if len(result) >= k else ""
