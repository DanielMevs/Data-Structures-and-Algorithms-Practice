from collections import deque


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] != '0':
            return False

        queue = deque([0])
        farthest = 0  # to make sure we're not repeating the same jump

        while queue:
            position = queue.popleft()

            start = max(position + minJump, farthest + 1)
            end = min(position + maxJump, len(s) - 1)

            for i in range(start, end + 1):
                if s[i] == '0':
                    if i == len(s) - 1:
                        return True
                    queue.append(i)

            farthest = end

        return False
