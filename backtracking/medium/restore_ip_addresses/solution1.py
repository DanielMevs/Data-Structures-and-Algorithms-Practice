from typing import List
IP_MAX_LENGTH = 12
TREE_MAX_HEIGHT = 4


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        if len(s) > IP_MAX_LENGTH:
            return result

        def backtrack(i, dots, currIP):
            if dots == TREE_MAX_HEIGHT and i == len(s):
                result.append(currIP[:-1])
                return
            if dots > 4:
                return

            for j in range(i, min(len(s), i + 3)):
                if int(s[i: j + 1]) <= 255 and (i == j or s[i] != '0'):
                    backtrack(j + 1, dots + 1, currIP + s[i: j + 1] + '.')

        backtrack(0, 0, '')
        return result
