from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        balls = moves = 0
        output = [0] * n

        for i in range(n):
            inc = balls + moves
            output[i] = inc
            if boxes[i] == '1':
                balls += 1
            moves = inc

        balls = moves = 0
        for i in range(n - 1, -1, -1):
            inc = balls + moves
            output[i] += inc
            if boxes[i] == '1':
                balls += 1
            moves = inc

        return output
