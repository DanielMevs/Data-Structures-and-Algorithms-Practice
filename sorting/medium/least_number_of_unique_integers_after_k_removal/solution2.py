from typing import List
from collections import Counter


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq_count = Counter(arr)
        freq_list = [0] * (len(arr) + 1)  # freq -> # of elements w/ that freq

        for _, freq in freq_count.items():
            freq_list[freq] += 1

        result = len(freq_count)

        for freq in range(1, len(freq_list)):
            remove = freq_list[freq]
            if k >= freq * remove:
                k -= freq * remove
                result -= remove
            else:
                remove = k // freq
                result -= remove
                break

        return result
