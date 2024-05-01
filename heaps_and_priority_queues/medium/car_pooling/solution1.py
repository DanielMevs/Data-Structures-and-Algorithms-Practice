from heapq import heappop, heappush


class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        trips.sort(key=lambda t: t[1])

        minHeap = []  # pair of [end, numPassengers]
        currentPassengers = 0
        for t in trips:
            numPass, start, end = t

            while minHeap and minHeap[0][0] <= start:
                currentPassengers -= minHeap[0][1]
                heappop(minHeap)

            currentPassengers += numPass

            if currentPassengers > capacity:
                return False
            heappush(minHeap, [end, numPass])

        return True