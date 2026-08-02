class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS=len(grid), len(grid[0])
        q=deque()
        fresh=0
        time=0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    q.append((r,c))

        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        while fresh>0 and q:
            for i in range(len(q)):
                r,c=q.popleft()
                for dr, dc in directions:
                    nr,nc=r+dr, c+dc
                    if (0<=nr<=ROWS-1 and 0<=nc<=COLS-1 
                        and grid[nr][nc]==1):
                        grid[nr][nc]=2
                        q.append((nr, nc))
                        fresh-=1
            time+=1
        return time if fresh==0 else -1
        #Time: O(m*n)
        #Space: O(m*n)



        