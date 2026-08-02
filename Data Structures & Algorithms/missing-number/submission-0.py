class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        num_set=set()
        for i in range(0, n+1):
            print(i)
            num_set.add(i)
        
        for n in nums:
            if n in num_set:
                num_set.remove(n)
        return num_set.pop()
        