class Solution:
    # 初始化
    # 前后缀不同
    # 前后缀相同
    # next 更新
    def nextTable(self, next: List[int], s: str)->None:
        #初始化
        j = 0 #前缀和末尾
        next[0] = 0
        for i in range(1, len(s)): #i 后缀和末尾
            while j > 0 and s[i] != s[j]:
                j = next[j-1]
            if s[i] == s[j]:
                j += 1
            next[i] = j


    def strStr(self, haystack: str, needle: str) -> int:
        hay_len,nee_len = len(haystack), len(needle)
        # boundary check 
        if nee_len == 0:
            return 0
        if hay_len < nee_len:
            return -1
        # 初始化
        next = [0] * nee_len
        self. nextTable(next, needle) # mutable data type can be changed
        # after they are created
        j = 0
        for i in range(hay_len):
            while j > 0 and haystack[i] != needle[j]:
                j = next[j-1]
            
            if haystack[i] == needle[j]:
                j += 1
            
            if j == nee_len:
                return i - nee_len + 1
        
        return -1

