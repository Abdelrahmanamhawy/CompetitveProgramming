class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        #Intalize first
        #DP=1D array . 
        dp=[0]*len(cost)
        dp[0]=cost[0]
        dp[1]=cost[1]
        
        
        for i in range(2,len(cost)):
            dp[i]=min(dp[i-1],dp[i-2])+(0 if i==len(cost) else cost[i])
            
        return min(dp[-2:])