class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res=len(nums)
        for i in range(len(nums)):
            res+=(i-nums[i])
        return res
        #Time: O(n)
        #Space: O(1)
            
           
        