class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s) < k:
            # create new string and assign to s
            return s[::-1]
        
        elif len(s) < 2*k:
            return s[:k][::-1] + s[k:]
        
        s = list(s)
        for i in range(0,len(s), 2*k):
            
            if len(s) - i < k:
                return "".join(s[:i] + s[i:][::-1])
            
            s[i:i+k] = s[i:i+k][::-1]
        
        return "".join(s)

