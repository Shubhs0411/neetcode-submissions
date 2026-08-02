class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS=len(grid)
        COLS=len(grid[0])
        directions=[[0,1],[1,0],[-1,0],[0,-1]]
        max_area=0

        def bfs(i,j):
            q=deque()
            q.append((i,j))
            grid[i][j]=0
            area=1

            while q:
                r,c=q.popleft()
                for dr,dc in directions:
                    nr,nc=r+dr,c+dc
                    if (0<=nr<ROWS and 0<=nc<COLS and grid[nr][nc]==1):
                        q.append((nr,nc))
                        grid[nr][nc]=0
                        area+=1
            return area
                    

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==1:
                    area=bfs(i,j)
                    max_area=max(max_area, area)
        return max_area