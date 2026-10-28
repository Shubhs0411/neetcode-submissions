class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMin, currMax=1,1
        res=nums[0]

        for i in range(len(nums)):
            tmp= currMax*nums[i]
            currMax=max(currMax*nums[i], currMin*nums[i], nums[i])
            currMin=min(tmp, currMin*nums[i], nums[i])
            res=max(res, currMax)
        return res