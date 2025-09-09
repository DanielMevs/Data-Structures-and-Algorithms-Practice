from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        folder_count = 0
        for folder in logs:
            if folder == './':
                continue
            elif folder == '../':
                stack.pop() if stack else 0
            else:
                stack.append(folder)

        while stack:  # count the directories left over
            folder_count += 1
            stack.pop()

        return folder_count
