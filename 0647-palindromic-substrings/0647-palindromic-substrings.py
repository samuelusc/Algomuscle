class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False] * len(s) for _ in range(len(s))]

        res = 0
        
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i < 2: 
                        dp[i][j] = True
                        res += 1
                    elif dp[i+1][j-1] == True:
                        dp[i][j] = True
                        res += 1

        return res               
                        