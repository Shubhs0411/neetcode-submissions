class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree=[0]*numCourses
        graph=defaultdict(list)

        for src, dst in prerequisites:
            graph[src].append(dst)
            indegree[dst]+=1

        q=deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        course_taken=0

        while q:
            course=q.popleft()
            course_taken+=1
            for neighbour in graph[course]:
                indegree[neighbour]-=1
                if indegree[neighbour]==0:
                    q.append(neighbour)
        return course_taken==numCourses
