class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp={}

        def dfs(i, prev):
            if i==len(nums):
                return 0
            if (i, prev) in dp:
                return dp[(i, prev)]
            skip=dfs(i+1, prev)
            take=0
            if prev==-1 or nums[prev]<nums[i]:
                take=1+dfs(i+1, i)
            
            res=max(take, skip)
            dp[(i, prev)]=res
            return res
        return dfs(0, -1)