from typing import List
from heapq import heappush, heappop


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        available = [i for i in range(n)]  # room 0, 1, 2, ..., n-1
        used = []  # (end_time, room_number)
        count = [0] * n  # count[n] = meetings scheduled

        for start, end in meetings:
            # Finish meetings
            while used and start >= used[0][0]:
                _, room = heappop(used)
                heappush(available, room)

            # no room is available
            if not available:
                end_time, room = heappop(used)
                end = end_time + (end - start)
                heappush(available, room)

            # a room is available
            room = heappop(available)
            heappush(used, (end, room))
            count[room] += 1

        return count.index(max(count))
