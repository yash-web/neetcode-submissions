class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)==0:
            return 0

        if len(cost)==1:
            return cost[0]
        res=[0 for i in range(len(cost)+2)]
        res[0]=0
        res[1]=cost[0]

        for i in range(1,len(cost)):

            res[i+1]=cost[i]+min(res[i],res[i-1])

        
        print(res)

        return min(res[len(cost)],res[len(cost)-1])
        