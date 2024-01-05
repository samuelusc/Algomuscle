# Day10 - Stack and Queue Part 1

## Contents
* [232. Implement Queue using Stacks](#232)
* [225. Implement Stack using Queues](#225)


<h2 id = "232"><a href="https://leetcode.com/problems/implement-queue-using-stacks">232. Implement Queue using Stacks</a></h2><h3>Easy</h3><p>Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (<code>push</code>, <code>peek</code>, <code>pop</code>, and <code>empty</code>).</p>

<p>Implement the <code>MyQueue</code> class:</p>

<ul>
	<li><code>void push(int x)</code> Pushes element x to the back of the queue.</li>
	<li><code>int pop()</code> Removes the element from the front of the queue and returns it.</li>
	<li><code>int peek()</code> Returns the element at the front of the queue.</li>
	<li><code>boolean empty()</code> Returns <code>true</code> if the queue is empty, <code>false</code> otherwise.</li>
</ul>

<p><strong>Notes:</strong></p>

<ul>
	<li>You must use <strong>only</strong> standard operations of a stack, which means only <code>push to top</code>, <code>peek/pop from top</code>, <code>size</code>, and <code>is empty</code> operations are valid.</li>
	<li>Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack&#39;s standard operations.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;MyQueue&quot;, &quot;push&quot;, &quot;push&quot;, &quot;peek&quot;, &quot;pop&quot;, &quot;empty&quot;]
[[], [1], [2], [], [], []]
<strong>Output</strong>
[null, null, null, 1, 1, false]

<strong>Explanation</strong>
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= x &lt;= 9</code></li>
	<li>At most <code>100</code>&nbsp;calls will be made to <code>push</code>, <code>pop</code>, <code>peek</code>, and <code>empty</code>.</li>
	<li>All the calls to <code>pop</code> and <code>peek</code> are valid.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow-up:</strong> Can you implement the queue such that each operation is <strong><a href="https://en.wikipedia.org/wiki/Amortized_analysis" target="_blank">amortized</a></strong> <code>O(1)</code> time complexity? In other words, performing <code>n</code> operations will take overall <code>O(n)</code> time even if one of those operations may take longer.</p>

#### Solving approach:
用两个栈实现Queue，helper() 将用来在两个栈中传输并将元素的输送延迟到必要时（Amortized Analysis) 

#### My Solution 1：_`2 stacks`_
```python
class MyQueue:
    # we need at least 2 stack to imitate queue's property
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)


    def pop(self) -> int:
        self._move()
        return self.stack_out.pop()

    def peek(self) -> int:
        self._move()
        return self.stack_out[-1]

    def empty(self) -> bool:
        # Don't need to call _move()
        return not self.stack_in and not self.stack_out

    # help function and private class function with _name
    def _move(self) -> None:
        # Move elements from stack in to stack out when stack_out is empty
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

```
- *`Time Complexity`*:
  </br>
  __init__: O(1) initialize two empty stacks take constant time.</br>
  **push()**: O(1) Append operation on a list(stack) costs an amortized constant time operation.</br>
  **pop()**: Amortized O(1). In the worst case, this can be O(n) since it hast to move all elements from stack_in to stack_out.However each element is only moved once 
and for m operations it gives average time complexity of O(1).</br>
  **peek()**: Amortized O(1) similar to pop().</br>
  **move**: Amortized O(1)
   
- *`Space Complexity`*:
</br>
**O(n)**

*****

<h2 id="225"><a href="https://leetcode.com/problems/implement-stack-using-queues">225. Implement Stack using Queues</a></h2><h3>Easy</h3><p>Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (<code>push</code>, <code>top</code>, <code>pop</code>, and <code>empty</code>).</p>

<p>Implement the <code>MyStack</code> class:</p>

<ul>
	<li><code>void push(int x)</code> Pushes element x to the top of the stack.</li>
	<li><code>int pop()</code> Removes the element on the top of the stack and returns it.</li>
	<li><code>int top()</code> Returns the element on the top of the stack.</li>
	<li><code>boolean empty()</code> Returns <code>true</code> if the stack is empty, <code>false</code> otherwise.</li>
</ul>

<p><b>Notes:</b></p>

<ul>
	<li>You must use <strong>only</strong> standard operations of a queue, which means that only <code>push to back</code>, <code>peek/pop from front</code>, <code>size</code> and <code>is empty</code> operations are valid.</li>
	<li>Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue&#39;s standard operations.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;MyStack&quot;, &quot;push&quot;, &quot;push&quot;, &quot;top&quot;, &quot;pop&quot;, &quot;empty&quot;]
[[], [1], [2], [], [], []]
<strong>Output</strong>
[null, null, null, 2, 2, false]

<strong>Explanation</strong>
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= x &lt;= 9</code></li>
	<li>At most <code>100</code> calls will be made to <code>push</code>, <code>pop</code>, <code>top</code>, and <code>empty</code>.</li>
	<li>All the calls to <code>pop</code> and <code>top</code> are valid.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow-up:</strong> Can you implement the stack using only one queue?</p>

#### Solving approach:
行为必须符合queue的先进先出，所以用两个queue 这样可以让最新的在对列前头。另外python 需要from collections import deque, 并使用 popleft() 从对列头部取出。

#### My Solution 1：_`2 queues`_
```python

class MyStack:
    from collections import deque
    def __init__(self):
        # Use two queues to implement the stack behavior
        self.main_queue = deque()
        self.helper_queue = deque()

    def push(self, x: int) -> None:
        self.helper_queue.append(x)

        while self.main_queue:
            self.helper_queue.append(self.main_queue.popleft())
        
        self.main_queue, self.helper_queue = self.helper_queue, self.main_queue
    #remove and retrun the last element which is at the start of the queue
    def pop(self) -> int:
        return self.main_queue.popleft()
    #return the first element in the queue 
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

```

- *`Time Complexity`*:
`push` : O(n) / `Others`: O(1)
- *`Space Complexity`*:
O(n)

