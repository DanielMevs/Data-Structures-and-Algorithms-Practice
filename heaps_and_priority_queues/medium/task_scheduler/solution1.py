# - Time complexity O(n * m) where n = task, m = idle time
from collections import Counter, deque
import heapq


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        # - Each task 1 unit time
        # - Minimize idle time

        taskCount = Counter(tasks)
        maxHeap = [-count for count in taskCount.values()]
        heapq.heapify(maxHeap)

        time = 0
        queue = deque()  #pairs of [-count, idleTime]

        while maxHeap or queue:
            time += 1

            if maxHeap:
                count = heapq.heappop(maxHeap)
                if count:
                    queue.append([count, time + n])
                
                if queue and queue[0][1] == time:
                    heapq.heappush(maxHeap, queue.popleft()[0])
        
        return time