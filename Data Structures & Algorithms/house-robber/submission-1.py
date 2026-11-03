class Solution:
    def rob(self, nums: List[int]) -> int:
        #edge cases:
        #nums=[4], res=4
        #nums=[], res=0
        #nums=[2,2,2], res=4


        dp={}
        

        def dfs(i):
            if i>=len(nums):
                return 0
            if i in dp:
                return dp[i]
            
            
            res=max(dfs(i+1), nums[i]+dfs(i+2))
            dp[i]=res
            return res
        return dfs(0)

        #Time: O(n)
        #Space: O(n)