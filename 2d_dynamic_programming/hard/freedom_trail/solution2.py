class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        dp = [0] * len(ring)
        for k in reversed(range(len(key))):
            curr_dp = [float('inf')] * len(ring)
            for r in range(len(ring)):
                for i, c in enumerate(ring):
                    if c == key[k]:
                        min_dist = min(
                            abs(r - i),  # between
                            len(ring) - abs(r - i)  # around
                        )
                        curr_dp[r] = min(
                            curr_dp[r],
                            min_dist + 1 + dp[i]
                        )
            dp = curr_dp
        return dp[0]
