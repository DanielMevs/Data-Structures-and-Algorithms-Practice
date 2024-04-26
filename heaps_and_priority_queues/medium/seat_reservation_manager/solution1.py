from heapq import heappop, heappush


class SeatManager:

    def __init__(self, n: int):
        self.unreserved = [i for i in range(1, n + 1)]

    def reserve(self) -> int:
        return heappop(self.unreserved)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.unreserved, seatNumber)

