class Solution:
    def trap(self, height: list[int]) -> int:
        # - Alternatively, we could have
        # initialized deques, which we could
        # use to dynamically push elements to
        # the front and back of our deque, instead
        # of creating three separate  list
        # comprehensions.
        maxLeft = [0 for _ in range(len(height))]
        maxRight = [0 for _ in range(len(height))]
        minLeftRight = [0 for _ in range(len(height))]

        for i in range(1, len(height)):
            maxLeft[i] = max(maxLeft[i - 1], height[i - 1])
        
        for i in range(len(height) - 2, -1, -1 ):
            maxRight[i] = max(maxRight[i + 1], height[i + 1])

        for i in range(len(height)):
            minLeftRight[i] = min(maxLeft[i], maxRight[i])

        result = 0

        for i, bucket in enumerate(height):
            water = minLeftRight[i] - bucket
            if water < 1:
                continue
            result += water
        
        return result
        