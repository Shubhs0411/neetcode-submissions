class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS=len(matrix), len(matrix[0])
        directions=[[1,0], [-1,0], [0,-1], [0,1]]
        dp=[[0]*COLS for _ in range(ROWS)]

        def dfs(r,c, preVal):
            if (r<0 or c<0 or r>=ROWS or c>=COLS or matrix[r][c]<=preVal):
                return 0

            res=float("-inf")
            if dp[r][c]!=0:
                return dp[r][c]

            
            if matrix[r][c]>preVal:
                for dr, dc in directions:
                    res=max(res, 1+dfs(r+dr, c+dc, matrix[r][c]))
            dp[r][c]=res
            return res
        
        final_res=float("-inf")
        for r in range(ROWS):
            for c in range(COLS):
                final_res=max(final_res, dfs(r,c,float("-inf")))
        return final_res
        

