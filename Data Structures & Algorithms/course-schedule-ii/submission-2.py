class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree=[0]*numCourses
        adj={i:[] for i in range(numCourses)}

        for crs,pre in prerequisites:
            adj[pre].append(crs)
            indegree[crs]+=1
        
        q=deque(i for i in range(numCourses) if indegree[i]==0)
        order=[]
        while q:
            course=q.popleft()
            order.append(course)
            for c in adj[course]:
                indegree[c]-=1
                if indegree[c]==0:
                    q.append(c)
        return order if len(order)==numCourses else []

        