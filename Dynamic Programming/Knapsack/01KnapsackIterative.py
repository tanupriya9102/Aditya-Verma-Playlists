# 0 - 1 Knapsack Problem on GFG


class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W
    
        
    def knapSack(self,W, wt, val, n):
        # code here
        dp=[[0 for _ in range(W+1)]for _ in range(n+1)]
        for i in range(1, n + 1):
            for w in range(1, W + 1):
                if wt[i - 1] <= w:
                    dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w])
                else:
                    dp[i][w] = dp[i - 1][w]
        return dp[n][W]
