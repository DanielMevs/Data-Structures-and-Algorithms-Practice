from typing import List


class Solution:
    # O(n * m) time, O(1) space
    # Key constraint: 0 <= img[i][j] <= 255
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows, cols = len(img), len(img[0])

        for r in range(rows):
            for c in range(cols):
                total, count = 0, 0
                for i in range(r - 1, r + 2):
                    for j in range(c - 1, c + 2):
                        if i < 0 or i == rows or j < 0 or j == cols:
                            continue
                        total += img[i][j] % 256  # take the lower 8 bits
                        count += 1
                img[r][c] ^= (total // count) << 8  # store in upper 8 bits

        for r in range(rows):
            for c in range(cols):
                img[r][c] = img[r][c] >> 8  # decode by discarding lower 8 bits

        return img
