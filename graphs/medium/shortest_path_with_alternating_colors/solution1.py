from typing import List
from collections import defaultdict, deque


class Solution:
    def shortestAlternatingPaths(
            self, n: int, redEdges: List[List[int]],
            blueEdges: List[List[int]]) -> List[int]:
        red = defaultdict(list)
        blue = defaultdict(list)

        for start, end in redEdges:
            red[start].append(end)
        for start, end in blueEdges:
            blue[start].append(end)

        answer = [-1] * n
        queue = deque()  # node, length, previous color
        queue.append([0, 0, None])
        visited = set()
        visited.add((0, None))

        while queue:
            node, length, edgeColor = queue.popleft()
            if answer[node] == -1:
                answer[node] = length

            if edgeColor != "RED":
                for neighbor in red[node]:
                    if (neighbor, "RED") not in visited:
                        queue.append([neighbor, length + 1, "RED"])
                        visited.add((neighbor, "RED"))
            if edgeColor != "BLUE":
                for neighbor in blue[node]:
                    if (neighbor, "BLUE") not in visited:
                        queue.append([neighbor, length + 1, "BLUE"])
                        visited.add((neighbor, "BLUE"))

        return answer
