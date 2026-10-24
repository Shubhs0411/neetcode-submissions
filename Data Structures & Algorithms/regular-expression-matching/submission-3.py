class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp={}

        def dfs(i,j):
            if j==len(p):
                return i==len(s)

            if (i,j) in dp:
                return dp[(i,j)]
            
            match= i<len(s) and (s[i]==p[j] or p[j]==".")

            if (j+1)<len(p) and p[j+1]=="*":
                res=(dfs(i,j+2) or (match and dfs(i+1,j)))
            else:
                res=match and dfs(i+1,j+1)
            
            dp[(i,j)]=res
            return res
        return dfs(0,0)

        #Time: O(m*n)
        #Space: O(m*n)
                

            

        