class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        memo={}

        def dfs(i,a):
            if a==0:
                return 1
            if i>=len(coins):
                return 0

            if (i,a) in memo:
                return memo[(i,a)]

            if a>=coins[i]:
                memo[(i,a)]=dfs(i+1,a)+dfs(i, a-coins[i])
            else:
                memo[(i,a)]=dfs(i+1,a)
            return memo[(i,a)]
        return dfs(0,amount)