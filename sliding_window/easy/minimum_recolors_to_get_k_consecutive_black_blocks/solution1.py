class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left, recolor = 0, 0
        result = k
        for right in range(len(blocks)):
            if blocks[right] == 'W':
                recolor += 1
            if right - left + 1 == k:
                result = min(recolor, result)
                recolor -= 1 if blocks[left] == 'W' else 0
                left += 1
        return result
