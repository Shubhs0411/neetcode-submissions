class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        prefix=1

        for i in range(len(nums)):
            res.append(prefix)
            prefix=prefix*nums[i]
        
        suffix=1
        for j in range(len(nums)-1,-1,-1):
            res[j]=res[j]*suffix
            suffix=suffix*nums[j]

        return res
        