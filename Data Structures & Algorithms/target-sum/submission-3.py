class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo={}

        def dfs(i, a):
            if i==len(nums):
                return 1 if a==0 else 0
            if (i,a) in memo:
                return memo[(i,a)]
            
            memo[(i,a)]=dfs(i+1, a-nums[i]) + dfs(i+1, a+nums[i])
            res=memo[(i,a)]
            return res

        return dfs(0,target)