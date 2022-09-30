class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}

        for course, pre in prerequisites:
            preMap[course].append(pre)
        #make the course / prerequisites MAP
        visited = set()
        #visited set for cycle if i found a cycle i cant complete all courses
        def dfs(course):
            if course in visited: #cycle return False
                return False
            if preMap[course] == []: #already see that course is valid
                return True

            visited.add(course) #add to visit for see follwing the neighbor i return to myself
            for pre in preMap[course]: #check neighbor / pre
                if not dfs(pre): return False
            visited.remove(course)  # i need it only for see cycle inside
            preMap[course] = [] #mark that course as valid
            return True

        for course, pre in prerequisites: #check if every course is valid with dfs
            if not dfs(course):
                return False
        return True