class Solution:
    def findOrder(
            self, numCourses: int,
            prerequisites: list[list[int]]) -> list[int]:
        # - Build an adjacency list of prereqs
        preReqs = {c: [] for c in range(numCourses)}
        for course, preReq in prerequisites:
            preReqs[course].append(preReq)
        
        output = []
        visited, cycle = set(), set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            
            cycle.add(course)
            for preReq in preReqs[course]:
                if not dfs(preReq):
                    return False
            cycle.remove(course)
            visited.add(course)
            output.append(course)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return output
                
