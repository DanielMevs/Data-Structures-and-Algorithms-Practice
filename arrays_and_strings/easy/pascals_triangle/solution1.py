class Solution:
    def generate(self, numRows: int) ->list[list[int]]:
        levels = []
        for i in range(numRows):
            row = [_ for _ in range(i + 1)]
            first, last = 0, i
            row[first] = 1
            row[last] = 1
            j = 1
            while j < i:
                row[j] = levels[i - 1][j - 1] + levels[i - 1][j]
                j += 1
            levels.append(row)

        return levels