from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # Sort the pairs based on their ending values.
        pairs.sort(key=lambda x: x[1])

        # Use a mutable container for the current end.
        current_end = [-float('inf')]

        # Define the filter function that updates the chain state.
        def valid(pair):
            # If the start of the pair is greater than the current end,
            # update the current end and include the pair.
            if pair[0] > current_end[0]:
                current_end[0] = pair[1]
                return True
            return False

        # Use filter to select pairs that can extend the chain.
        chain = list(filter(valid, pairs))
        return len(chain)
