class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c=[0]*26

        for string in s:
            c[ord(string)-ord('a')]+=1
        for string in t:
            c[ord(string)-ord('a')]-=1

        for i in range(len(c)):
            if c[i]!=0:
                return False
        return True
        