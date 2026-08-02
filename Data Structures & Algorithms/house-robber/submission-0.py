class Solution:
    def rob(self, nums: List[int]) -> int:
        
        rob1, rob2 = 0, 0  # rob1 = max rob till i-2, rob2 = max till i-1

        for n in nums:
            new_rob = max(rob1 + n, rob2)  # Either rob this house or skip
            rob1 = rob2
            rob2 = new_rob
        
        return rob2

            


        