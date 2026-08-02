class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=defaultdict(list)
        in_degree=[0]*numCourses

        for main,preq in prerequisites:
            graph[preq].append(main)
            in_degree[main]+=1
        
        queue=deque([i for i in range(numCourses) if in_degree[i]==0])
        courses_taken=0

        while queue:
            course=queue.popleft()
            courses_taken+=1
            for neighbor in graph[course]:
                in_degree[neighbor]-=1
                if in_degree[neighbor]==0:
                    queue.append(neighbor)
        return courses_taken==numCourses
            
        