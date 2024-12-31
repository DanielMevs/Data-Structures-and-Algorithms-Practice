from typing import List


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        stickCount = []
        for i, s in enumerate(stickers):
            stickCount.append({})
            for c in s:
                stickCount[i][c] = stickCount[i].get(c, 0) + 1

        dp = {}  # key = subseq of target | val = min num of stickers

        def dfs(t, stick):
            if t in dp:
                return dp[t]

            result = 1 if stick else 0
            remainTarget = ''
            for c in t:
                if c in stick and stick[c] > 0:
                    stick[c] -= 1
                else:
                    remainTarget += c

            if remainTarget:
                used = float('inf')
                for s in stickCount:
                    if remainTarget[0] not in s:
                        continue
                    used = min(dfs(remainTarget, s.copy()), used)
                dp[remainTarget] = used
                result += used

            return result

        result = dfs(target, {})
        return result if result != float('inf') else -1
