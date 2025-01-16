class Solution:
    #  Time complexity: O(N), space complexity: O(N)
    def numberOfWays(self, corridor: str) -> int:
        mod = 10**9 + 7
        seats = []  # index of each seat
        for i, c in enumerate(corridor):
            if c == 'S':
                seats.append(i)

        length = len(seats)
        if length < 2 or length % 2 == 1:
            return 0

        # count valid combinations
        result = 1
        i = 1
        while i < length - 1:
            result *= seats[i + 1] - seats[i]
            i += 2

        return result % mod
