class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        rows, cols=len(grid),len(grid[0])
        visited=set()
        
        def bfs(r,c):
            q=deque([(r,c)])
            visited.add((r,c))
            perimeter=0
            
            while q:
                x,y=q.popleft()
                for dr,dc in directions:
                    nr,nc=x+dr,y+dc
                    if (nr<0 or nc<0 or nr>=rows or nc>=cols or grid[nr][nc]==0):
                        perimeter+=1
                    elif (nr,nc) not in visited:
                        visited.add((nr,nc))
                        q.append((nr,nc))
            return perimeter

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    return bfs(i,j)
        return 0


        