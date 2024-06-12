class Solution:
    def calculate(self, s: str) -> int:
        
        def helper(s: deque) -> int:
            stack = []
            num = 0
            sign = "+"

            while s:
                char = s.popleft()
                
                if char.isdigit():
                    num = 10 * num + int(char)
                
                if char == "(":
                    num  = helper(s)
                
                if (not char.isdigit() and char != " ") or not s:
                    if sign == "+":
                        stack.append(num)

                    elif sign == "-":
                        stack.append(-num)

                    elif sign == "*":
                        stack[-1] *= num

                    elif sign == "/":
                        stack[-1] = int(stack[-1]/num)
                    
                    num = 0
                    sign = char
                
                if char == ")":
                    break
                
            return sum(stack)
        
        return helper(collections.deque(s))


        