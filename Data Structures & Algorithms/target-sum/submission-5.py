class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp={} #(i, a)-> ways

        def dfs(i, a):
            if i==len(nums):
                return 1 if a==0 else 0
            if (i, a) in dp:
                return dp[(i,a)]
            
            res=dfs(i+1, a-nums[i])+dfs(i+1, a+nums[i])
            dp[(i,a)]=res
            return dp[(i,a)]
        return dfs(0, target)
        #Time: O(n*m)
        #Space: O(n*m)