from typing import List
from collections import defaultdict


class Solution:
    def checkIfPrerequisite(
            self, numCourses: int,
            prerequisites: List[List[int]],
            queries: List[List[int]]) -> List[bool]:

        adjacent = defaultdict(list)
        for prereq, crs in prerequisites:
            adjacent[crs].append(prereq)

        def dfs(crs):
            if crs not in prereqMap:
                prereqMap[crs] = set()
                for prereq in adjacent[crs]:
                    prereqMap[crs] |= dfs(prereq)  # union of sets
                prereqMap[crs].add(crs)

            return prereqMap[crs]
        prereqMap = {}  # map crs => hashset of indirect prereqs
        for crs in range(numCourses):
            dfs(crs)

        result = []
        for val, query in queries:
            result.append(val in prereqMap[query])

        return result
