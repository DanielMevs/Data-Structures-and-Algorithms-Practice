class Solution:
    def canFinish(
            self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # - Map each course to pre-requisite list
        preMap = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            preMap[course].append(prereq)
        
        # - visitSet = all courses along the curr DFS path
        visitSet = set()

        def dfs(course):
            if course in visitSet:
                return False
            if preMap[course] == []:
                return True
            
            visitSet.add(course)
            for preReq in preMap[course]:
                if not dfs(preReq):
                    return False
            visitSet.remove(course)
            preMap[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True