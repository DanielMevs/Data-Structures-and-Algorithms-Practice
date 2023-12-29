from collections import deque

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        pieces = list(dominoes)
        queue = deque()

        for i, domino in enumerate(pieces):
            if domino != '.':
                queue.append((i, domino))
        
        while queue:
            i, domino = queue.popleft()

            if domino == 'L' and i > 0 and pieces[i - 1] == '.':
                queue.append((i - 1, 'L'))
                pieces[i - 1] = 'L'

            elif domino == "R":
                if i + 1 < len(pieces) and pieces[i + 1] == '.':
                    if i + 2 < len(pieces) and pieces[i + 2] == 'L':
                        queue.popleft()
                    else:
                        queue.append((i + 1, 'R'))
                        pieces[i + 1] = 'R'
        
        return ''.join(pieces)

        