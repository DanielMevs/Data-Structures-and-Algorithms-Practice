from typing import List
START = 11
END = 12 + 1
TARGET = 60


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for detail in details:
            if int(detail[START: END]) > TARGET:
                count += 1
        return count
