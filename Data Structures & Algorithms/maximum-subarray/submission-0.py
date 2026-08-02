class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum, maxSum=0, nums[0]
        for i in range(len(nums)):
            if currSum<0:
                currSum=0
            currSum+=nums[i]
            maxSum=max(maxSum, currSum)
        return maxSum
        #Time: O(n)
        #Space: O(1)