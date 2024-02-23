class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        # initialization
        dp = [[0] * (n+1) for _ in range(m+1)]

        for char in strs:
            # count the number of '1' and '0'
            zeros = char.count('0')
            ones = char.count('1')

            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):

                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)

        
        return dp[m][n]
