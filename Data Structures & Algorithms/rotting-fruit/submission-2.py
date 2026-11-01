class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #not grid, return None
        # the values contains negatives, no
        #if no fresh, return 0
        ROWS, COLS=len(grid), len(grid[0])
        directions=[[1,0],[-1,0],[0,1],[0,-1]]
        q=deque()
        fresh=0
        time=0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    fresh+=1
                elif grid[r][c]==2:
                    q.append((r,c))

        while q and fresh>0:
            for i in range(len(q)):
                r,c=q.popleft()

                for dr,dc in directions:
                    nr,nc=dr+r, dc+c
                    if (nr<0 or nc<0 or nr>=ROWS or nc>=COLS or grid[nr][nc]!=1):
                        continue

                    grid[nr][nc]=2
                    fresh-=1
                    q.append((nr,nc))
            time+=1
        return time if fresh==0 else -1
                    
