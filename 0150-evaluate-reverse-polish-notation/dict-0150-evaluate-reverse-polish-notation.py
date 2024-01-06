class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        import operator
        def is_digit(s):
            if s[0] == '-':
                return s[1:].isdigit()
            return s.isdigit()
        stack = []
        # / 1. operator.truedive(/) 2. floordive (//)
        # 3. lambda x,y: int(operator.truediv(x,y)) truncates toward zero
        operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': lambda x,y: int(operator.truediv(x, y))}
        for token in tokens:
            if  is_digit(token):
                stack.append(int(token))
            
            elif token in operators:
                num1 = stack.pop()
                num2 = stack.pop()
                # operators['+'](10, 5)  # 等于 10 + 5
                stack.append(operators[token](num2,num1))
            else:
                raise ValueError('Invalid token')

        return stack[-1]
