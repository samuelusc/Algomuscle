class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = [float('inf')]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

        
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            raise IndexError("Attempt to access top from an empty stack")

    def getMin(self) -> int:
        if self.stack:
            return self.min_stack[-1]
        else:
            raise IndexError("Attempt to access top from an  empty stack")


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()