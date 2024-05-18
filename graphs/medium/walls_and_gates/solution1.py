from collections import deque


class Solution:
    def wallsAndGates(self, rooms: list[list[int]]) -> None:
        ROWS, COLS = len(rooms), len(rooms[0])
        visited = set()
        gates = deque()

        def addRoom(r, c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or
               (r, c) in visited or rooms[row][col] == -1):
                return
            visited.add((r, c))
            gates.append([r, c])

        for row in range(ROWS):
            for col in range(COLS):
                if rooms[row][col] == 0:
                    gates.append([row, col])
                    visited.add((row, col))
        distance = 0
        while gates:
            for i in range(len(gates)):
                row, col = gates.popleft()
                rooms[row][col] = distance
                addRoom(row + 1, col)
                addRoom(row - 1, col)
                addRoom(row, col + 1)
                addRoom(row, col - 1)
            
            distance += 1
