class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map={}

        for i,num in enumerate(nums):
            diff=target-num
            if diff in nums_map:
                return [nums_map[diff], i]
            nums_map[num]=i
        return -1