class Solution:
    def nextTable(self, next:List[int], targetStr: str)-> None:
            j = 0
            next[0] = 0

            for i in range(1, len(targetStr)):
                while j>0 and targetStr[i] != targetStr[j]:
                    j= next[j-1]
                
                if targetStr[i] == targetStr[j]:
                    j += 1
                
                next[i] = j

    def repeatedSubstringPattern(self, s: str) -> bool:
        # constraints s.len <=1

        next = [0] * len(s)
        self.nextTable(next, s)

        # first statement 保证有重复
        # second 可以被最长前后缀之外的部分整除
        if next[-1] !=0 and len(s) % (len(s) - next[-1]) == 0 :
            return True
        
        return False
   
        

        

        