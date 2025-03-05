class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice, bob = 0, 0
        left = 0

        for right in range(len(colors)):
            if colors[left] != colors[right]:
                left = right
            extra = right - left + 1 - 2
            if extra > 0:
                if colors[right] == 'A':
                    alice += extra
                else:
                    bob += extra

        return alice > bob
