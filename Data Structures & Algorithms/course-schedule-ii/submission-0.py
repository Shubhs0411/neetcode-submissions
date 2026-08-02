class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        in_dregree=[0]*numCourses

        for main, preq in prerequisites:
            graph[preq].append(main)
            in_dregree[main]+=1

        order=[]
        queue=deque([i for i in range(numCourses) if in_dregree[i]==0])
        courses_taken=0

        while queue:
            course=queue.popleft()
            courses_taken+=1
            order.append(course)

            for neighbour in graph[course]:
                in_dregree[neighbour]-=1
                if in_dregree[neighbour]==0:
                    queue.append(neighbour)
        return order if len(order)==numCourses else[]
        