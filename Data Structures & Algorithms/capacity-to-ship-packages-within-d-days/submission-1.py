class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #edge cases:
        #weights=[7], days=1, res=7
        #weights=[1,2,3] days=1, res=6 sum of all
        #weights=[1,2,3] days=3, res=3 max

        def canShip(num):
            needed,curr_sum=1, 0
            for i in range(len(weights)):
                curr_sum+=weights[i]
                if curr_sum>num:
                    needed+=1
                    curr_sum=weights[i]
            return needed<=days

        l,r=max(weights), sum(weights)

        while l<r:
            mid=(l+r)//2

            if canShip(mid):
                r=mid
            else:
                l=mid+1
        return l


        #weights = [2,4,6,1,3,10], days = 4, output=10
        #max=10, sum=26, mid=18
        #canship(18)=1+1=2
        #canship(14)=1+1=2
        #canship(12)=1+1+1=3
        #canship(11)=1+1+1=3
        #canship(10)=1+1+1=3
        #3<=4
        #return 10, output 10