class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp={}
        def dfs(a):
            if a==0:
                return 0
            if a in dp:
                return dp[a]
            res=float("inf")
            for c in coins:
                if c<=a:
                    res=min(res, 1+dfs(a-c))
                
            dp[a]=res
            return res
        final_res=dfs(amount)
        return final_res if final_res!=float("inf") else -1