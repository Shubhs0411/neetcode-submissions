class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0],nums[1])

        def rob_lines(houses):
            rob1, rob2=0,0
            for n in houses:
                new_rob=max(rob1+n,rob2)
                rob1=rob2
                rob2=new_rob
            return rob2

        case1=rob_lines(nums[:-1])
        case2=rob_lines(nums[1:])

        return max(case1,case2)

        