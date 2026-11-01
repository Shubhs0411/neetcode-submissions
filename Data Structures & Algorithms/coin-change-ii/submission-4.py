class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #edge cases:
        #coins=[1], amount=5 res=1
        #coins=[], amount=4 res=0
        #coins=[4,10] amount=2 res=0
        #coins=[1,2] amount =0 res=1

        coins.sort()
        dp={}

        def dfs(i,a):
            if a==0:
                return 1
            if i>=len(coins):
                return 0
            
            if (i,a) in dp:
                return dp[(i,a)]
            
            res=0
            if a>=coins[i]:
                res=dfs(i+1,a)
                res+=dfs(i, a-coins[i])
            
            dp[(i,a)]=res
            return res
        return dfs(0,amount)
