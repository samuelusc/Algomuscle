class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * len(s)
        wordSet = set(wordDict)

        for i in range(1, len(s)+1):
            for j in range(i):
                word = s[j:i]

                if word in wordSet and dp[j]:
                    dp[i] = True
        
        return dp[-1]