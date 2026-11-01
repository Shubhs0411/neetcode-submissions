class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #not grid, return 0
        #if no fresh, return 0
        #unreachable -1
        # several rotten at start → all go in q at time 0 and spread together
        if not grid:
            return 0
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

    #Time: O(m*n)
    #Space: O(m*n)

    #[[1,1,0],[0,1,1],[0,1,2]]
    #q=[(2,2)], time=0, fresh=5, grid=[[1,1,0],[0,1,1],[0,1,2]]
    #q=[(1,2),(2,1)], time=1, fresh=3, grid=[[1,1,0],[0,1,2],[0,2,2]]
    #q=[(1,1)], time=2, fresh=2, grid=[[1,1,0],[0,2,2],[0,2,2]]
    #q=[(0,1)], time=3, fresh=1, grid=[[1,2,0],[0,2,2],[0,2,2]]
    #q=[(0,0)], time=4, fresh=0, grid=[[2,2,0],[0,2,2],[0,2,2]]

                    
