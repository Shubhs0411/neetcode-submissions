class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        xorr=n
        for i in range(len(nums)):
            xorr^=i^nums[i]
        return xorr
        #Time: O(n)
        #Space: O(1)
            
           
        