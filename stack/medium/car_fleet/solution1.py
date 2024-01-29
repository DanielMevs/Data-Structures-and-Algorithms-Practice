class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pair = [[pos, spd] for pos, spd in zip(position, speed)]
        stack = []

        # - Reverse sorted order
        for pos, spd in sorted(pair)[::-1]:
            stack.append((target - pos) / spd)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
                
        return len(stack)