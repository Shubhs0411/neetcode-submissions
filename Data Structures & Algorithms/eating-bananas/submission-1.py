class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1, max(piles)

        while l<r:
            mid=(l+r)//2
            curr_h=0

            for p in piles:
                curr_h+=math.ceil(p/mid)

            if curr_h<=h:
                r=mid
            else:
                l=mid+1
        return l