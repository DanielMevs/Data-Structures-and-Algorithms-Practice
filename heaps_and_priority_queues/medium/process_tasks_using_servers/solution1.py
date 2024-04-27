from heapq import heapify, heappop, heappush


class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        # Two min heaps, one for available server, one for unavailable
        # available = (weight, index)
        # unavailable = (timeServerBecomesFree, weight, index)

        result = [0] * len(tasks)

        available = [(servers[i], i) for i in range(len(servers))]
        heapify(available)
        unavailable = []

        t = 0
        for i in range(len(tasks)):
            t = max(t, i)

            if len(available) == 0:
                # - Updates t to time when next server become available
                t = unavailable[0][0]

            while unavailable and t >= unavailable[0][0]:
                timeFree, weight, index = heappop(unavailable)
                heappush(available, (weight, index))
            
            weight, index = heappop(available)
            result[i] = index
            heappush(unavailable, (t + tasks[i], weight, index))

        return result

