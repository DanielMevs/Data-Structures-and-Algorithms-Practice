from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        charSet = set()

        def overlap(charSet, s):
            prev = set()
            for char in s:
                if char in charSet or char in prev:
                    return True
                prev.add(char)
            return False

        def backtrack(i):
            if i == len(arr):
                return len(charSet)

            result = 0
            if not overlap(charSet, arr[i]):
                for char in arr[i]:
                    charSet.add(char)
                result = backtrack(i + 1)
                for char in arr[i]:
                    charSet.remove(char)

            return max(result, backtrack(i + 1))  # don't concatenate arr[i]

        return backtrack(0)
