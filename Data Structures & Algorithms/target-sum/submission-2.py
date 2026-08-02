class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp=defaultdict(int)
        dp[0]=1

        for num in nums:
            newDp=defaultdict(int)
            for total, count in dp.items():
                newDp[total+num]+=count
                newDp[total-num]+=count
            dp=newDp
        return dp[target]
        #Time: O(m*n)
        #Space: O(m)
        