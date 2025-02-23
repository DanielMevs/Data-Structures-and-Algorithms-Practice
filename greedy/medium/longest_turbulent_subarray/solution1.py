from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        left, right = 0, 1
        result, prev = 1, ""
        while right < len(arr):
            if arr[right - 1] > arr[right] and prev != ">":
                result = max(result, right - left + 1)
                right += 1
                prev = ">"
            elif arr[right - 1] < arr[right] and prev != "<":
                result = max(result, right - left + 1)
                right += 1
                prev = "<"
            else:
                right = right + 1 if arr[right] == arr[right - 1] else right
                left = right - 1
                prev = ""

        return result
