class Solution:    
    def isValid(self, s: str) -> bool:
        hash_table = {'(': ')', '{':'}', '[':']'}
        stack = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                
                stack.append(char)
                continue
            
            if stack:
                c_pop = stack.pop()
                if hash_table[c_pop] != char:
                    return False
                continue

            return False

        
        if not stack:
            return True
        else:
            return False
                


                