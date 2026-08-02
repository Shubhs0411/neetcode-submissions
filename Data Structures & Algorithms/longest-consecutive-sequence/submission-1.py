class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxres=0
        seen=set(nums)
        for num in seen:
            if num-1 not in seen:
                res=1
                while num+1 in seen:
                    res+=1
                    num=num+1
                maxres=max(res,maxres)
        return maxres