class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks)
        maxHeap=[-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        q=deque()
        time=0

        while q or maxHeap:
            if not maxHeap:
                time=q[0][1]
            else:
                cnt=1+heapq.heappop(maxHeap)
                if cnt:
                    q.append((cnt, time+n))

            if q and q[0][1]==time:
                cnt,_=q.popleft()
                heapq.heappush(maxHeap, cnt)
            time+=1
        return time
        