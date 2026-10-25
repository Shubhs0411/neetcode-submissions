class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals=sorted(zip(startTime, endTime, profit))
        dp={}

        def dfs(i):
            if i==len(intervals):
                return 0

            if i in dp:
                return dp[i]
            
            skip=dfs(i+1)
            
            j=i+1
            while j<len(intervals) and intervals[i][1]>intervals[j][0]:
                j+=1
            take=intervals[i][2]+dfs(j)

            res=max(skip, take)
            dp[i]=res
            return res  
        return dfs(0)          
            
