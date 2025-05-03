from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix_diff = [0] * (len(s) + 1)
        for start, end, d in shifts:
            prefix_diff[end + 1] += 1 if d else -1
            prefix_diff[start] += -1 if d else 1  # to counteract prev shift

        result = [ord(c) - ord('a') for c in s]
        diff = 0
        for i in reversed(range(len(prefix_diff))):
            diff += prefix_diff[i]
            result[i - 1] = (diff + result[i - 1]) % 26

        s = [chr(ord('a') + n) for n in result]
        return ''.join(s)
