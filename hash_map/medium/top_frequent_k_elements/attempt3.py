from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        result = sorted(count.keys(), key=count.get, reverse=True)
        for i in range(len(result)-k):
            result.pop()
        return result