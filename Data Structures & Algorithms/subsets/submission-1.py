class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]

        subset=[]

        def dfs(i):
            if i>=len(nums):
                res.append(subset.copy())
                return 

          #add i to the subset
            subset.append(nums[i])
            dfs(i+1)

            #remove i from the subset
            subset.pop()
            dfs(i+1)
        dfs(0)

        return res
        #Time: O(n*2^n)
        #Space: O(2^n)

        
        