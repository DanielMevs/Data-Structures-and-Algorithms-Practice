import heapq


class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        for i, t in enumerate(tasks):
            t.append(i)

        tasks.sort(key=lambda t: t[0])

        result, minHeap = [], []
        i, time = 0, tasks[0][0]

        while minHeap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(minHeap, [tasks[i][1], tasks[i][2]])
                i += 1
            
            if not minHeap:
                time = tasks[i][0]

            else:
                procTime, index = heapq.heappop(minHeap)
                time += procTime
                result.append(index)
        
        return result