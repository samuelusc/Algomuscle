class Solution:
    def calculate(self, s: str) -> int:
        stack = [] # Initialize an empty list to be used as a stack
        operator, res = 1, 0 # Operator starts as 1 for positive numbers and initialize cumulative result to be 0
        index, length = 0, len(s)

        # Iterate over the input string
        while index < length:
            # If the current character is a digit
            if s[index].isdigit():
                num = 0 
                # Continue until a non-digits is found, building the full number
                while index < length and s[index].isdigit():
                    num = num * 10 + int(s[index])
                    index += 1
                # update the result with the current number and the prededing operator
                res += num * operator
                # Decrement index to correcct the position after the inner loop overruns.
                index -= 1
            # if the current character is a plus, set operator to 1
            elif s[index] == "+":
                operator = 1
            # if the current character is a minus , set operator to -1(subtraction)
            elif s[index] == "-":
                operator = -1
            # handle opening parentheses
            elif s[index] == "(":
                # push the current result and operator to the stack
                stack.append(res)
                stack.append(operator)
                #reset the result and operator for the new expression within the parentheses
                res = 0
                operator = 1
            # handle closing parentheses
            elif s[index] == ")":
                # the result inside the parentheses is multiplied by the operator before the parentheses
                res *= stack.pop()
                # Add the result inside the parentheses to the result before the parentheses
                res += stack.pop()
            # move to the next character
            index += 1
        # return the evaluated result
        return res 



