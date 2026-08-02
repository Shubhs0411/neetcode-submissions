class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS=len(grid)
        COLS=len(grid[0])
        directions=[[0,1],[1,0],[0,-1],[-1,0]]
        INF = 2147483647
        q=deque()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==0:
                    q.append((i,j,0))

        while q:
            r,c,dist=q.popleft()
            
            for dr,dc in directions:
                nr,nc=r+dr, c+dc
                if (0<=nr<ROWS and 0<=nc<COLS and grid[nr][nc]==INF):
                    grid[nr][nc]=dist+1
                    q.append((nr,nc,dist+1))
                    

                    

