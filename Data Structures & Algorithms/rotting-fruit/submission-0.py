class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions=[[1,0],[0,1],[-1,0],[0,-1]]
        rows,cols=len(grid),len(grid[0])
        fresh=0
        minutes=0
        queue=deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    queue.append((r,c,0))
                elif grid[r][c]==1:
                    fresh+=1
        while queue:
            r,c,t=queue.popleft()
            minutes=max(minutes,t)
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                    grid[nr][nc]=2
                    fresh-=1
                    queue.append((nr,nc,t+1))

        return minutes if fresh==0 else -1
            




        