class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        list_s = list(s)
        for i in range(0, len(list_s), 2*k):
            list_s[i:i+k] = reversed(list_s[i:i+k])
        
        return "".join(list_s)