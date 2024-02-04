class MyStack:
    from collections import deque
    def __init__(self):
        self.main_queue = deque()
        self.helper_queue = deque()

    def push(self, x: int) -> None:
        self.helper_queue.append(x)

        while self.main_queue:
            self.helper_queue.append(self.main_queue.popleft())
        
        self.main_queue, self.helper_queue = self.helper_queue, self.main_queue

    def pop(self) -> int:
        return self.main_queue.popleft()

    def top(self) -> int:
        return self.main_queue[0]

    def empty(self) -> bool:
        return not self.main_queue


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
