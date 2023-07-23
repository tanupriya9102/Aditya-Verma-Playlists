class Solution:
    
    def knapSack(self, W, wt, val, n):
        dp = [[-1 for _ in range(n + 1)] for _ in range(W + 1)]

        def knapSackDp(W, wt, val, n):
            if W == 0 or n == 0:
                return 0
            
            if dp[W][n] != -1:
                return dp[W][n]
            
            if wt[n - 1] <= W:
                dp[W][n] = max(val[n - 1] + knapSackDp(W - wt[n - 1], wt, val, n - 1), knapSackDp(W, wt, val, n - 1))
            else:
                dp[W][n] = knapSackDp(W, wt, val, n - 1)

            return dp[W][n]

        return knapSackDp(W, wt, val, n)


# Example usage:
W = 7
wt = [1, 2, 3, 4, 5]
val = [10, 20, 30, 40, 50]
n = len(wt)
sol = Solution()
print(sol.knapSack(W, wt, val, n))  # Output: 90
