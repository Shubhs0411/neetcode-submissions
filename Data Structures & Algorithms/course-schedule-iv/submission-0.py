class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        indegree=[0]*numCourses
        adj=[[] for _ in range(numCourses)]

        for pre, crs in prerequisites:
            adj[pre].append(crs)
            indegree[crs]+=1

        q=deque([i for i in range(numCourses) if indegree[i]==0])
        prereq={i:set() for i in range(numCourses)}
        answer=[]

        while q:
            node=q.popleft()

            for nei in adj[node]:
                prereq[nei].add(node)
                prereq[nei]|=prereq[node]
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        
        for pre,crs in queries:
            if pre in prereq[crs]:
                answer.append(True)
            else:
                answer.append(False)
        return answer

        #Time:O(N*P+Q)
        #Space: O(N^2+P+Q)


        
        