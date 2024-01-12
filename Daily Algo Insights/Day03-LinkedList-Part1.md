# Day03 - LinkedList Part 1


## Contents
* **[203.Remove Linked List Elements](#203)**
* **[707.Design Linked List](#707)**
* **[206.Reverse Linked List](#206)**


<br>
<h2 id = "203"><a href="https://leetcode.com/problems/remove-linked-list-elements">203. Remove Linked List Elements</a></h2><h3>Easy</h3><p>Given the <code>head</code> of a linked list and an integer <code>val</code>, remove all the nodes of the linked list that has <code>Node.val == val</code>, and return <em>the new head</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/06/removelinked-list.jpg" style="width: 500px; height: 142px;" />
<pre>
<strong>Input:</strong> head = [1,2,6,3,4,5,6], val = 6
<strong>Output:</strong> [1,2,3,4,5]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> head = [], val = 1
<strong>Output:</strong> []
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> head = [7,7,7,7], val = 7
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[0, 10<sup>4</sup>]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 50</code></li>
	<li><code>0 &lt;= val &lt;= 50</code></li>
</ul>

### My Solution 1：_`dummy`_  

  
```python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 建立dummy 方便检查头节点
        dummy = ListNode(next = head)
        cur_node = dummy

        #需要有pre_node
        while cur_node.next:
            if cur_node.next.val == val:
                cur_node.next = cur_node.next.next

            # 保证next节点不是target
            else:
                cur_node = cur_node.next
        
        return dummy.next

                      
```


### My Solution 2：_`without dummy`_  

  
```python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # if we don't use dummy node

        # Don't use if such as [7,7,7,7] target 7
        while head and head.val == val:
            head = head.next
                
        cur_node = head

        while cur_node and cur_node.next:
            if cur_node.next.val == val:
                cur_node.next = cur_node.next.next
            

            else:
                cur_node = cur_node.next
        
        return head
```




**Complexity Analysis:**  

- *`Time Complexity`*:
O(n)
  
- *`Space Complexity`*:
O(1)
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)



<h2 id = "707"><a href="https://leetcode.com/problems/design-linked-list">707. Design Linked List</a></h2><h3>Medium</h3><p>Design your implementation of the linked list. You can choose to use a singly or doubly linked list.<br />
A node in a singly linked list should have two attributes: <code>val</code> and <code>next</code>. <code>val</code> is the value of the current node, and <code>next</code> is a pointer/reference to the next node.<br />
If you want to use the doubly linked list, you will need one more attribute <code>prev</code> to indicate the previous node in the linked list. Assume all nodes in the linked list are <strong>0-indexed</strong>.</p>

<p>Implement the <code>MyLinkedList</code> class:</p>

<ul>
	<li><code>MyLinkedList()</code> Initializes the <code>MyLinkedList</code> object.</li>
	<li><code>int get(int index)</code> Get the value of the <code>index<sup>th</sup></code> node in the linked list. If the index is invalid, return <code>-1</code>.</li>
	<li><code>void addAtHead(int val)</code> Add a node of value <code>val</code> before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.</li>
	<li><code>void addAtTail(int val)</code> Append a node of value <code>val</code> as the last element of the linked list.</li>
	<li><code>void addAtIndex(int index, int val)</code> Add a node of value <code>val</code> before the <code>index<sup>th</sup></code> node in the linked list. If <code>index</code> equals the length of the linked list, the node will be appended to the end of the linked list. If <code>index</code> is greater than the length, the node <strong>will not be inserted</strong>.</li>
	<li><code>void deleteAtIndex(int index)</code> Delete the <code>index<sup>th</sup></code> node in the linked list, if the index is valid.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;MyLinkedList&quot;, &quot;addAtHead&quot;, &quot;addAtTail&quot;, &quot;addAtIndex&quot;, &quot;get&quot;, &quot;deleteAtIndex&quot;, &quot;get&quot;]
[[], [1], [3], [1, 2], [1], [1], [1]]
<strong>Output</strong>
[null, null, null, null, 2, null, 3]

<strong>Explanation</strong>
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1-&gt;2-&gt;3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1-&gt;3
myLinkedList.get(1);              // return 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= index, val &lt;= 1000</code></li>
	<li>Please do not use the built-in LinkedList library.</li>
	<li>At most <code>2000</code> calls will be made to <code>get</code>, <code>addAtHead</code>, <code>addAtTail</code>, <code>addAtIndex</code> and <code>deleteAtIndex</code>.</li>
</ul>



### My Solution 1：_`xxx`_  

  
```python

class MyLinkedList:
    #design scratch 
    def __init__(self):
        # Create a dummy node
        self.dummy_node = ListNode()
        # Initialize node counter and length
        self.size = 0

    def get(self, index: int) -> int:
        # Boundary check
        if index < 0 or index >= self.size:
            return  -1

        # Start from the head, there will be at least one node
        current_node = self.dummy_node.next

        # Iterate to the next node based on index
        for _ in range(index):
            current_node = current_node.next
        
        return current_node.val

    def addAtHead(self, val: int) -> None:
        # Invoke addAtIndex and assign (0, val)
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        # Invoke addAtIndex and assign (self.size, val)
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        # Check for index out of bounds
        if index < 0 or index > self.size:
            return
        
        # Assign the dummy node to predecessor
        predecessor = self.dummy_node

        # Find the predecessor of the node to be added
        for _ in range(index):
            predecessor = predecessor.next
        
        # Create the new node and maintain the predecessor's link
        add_node = ListNode(val, predecessor.next)
        # Link the predecessor with the new node
        predecessor.next = add_node

        # Don't forget to increment self.size by 1 for each added node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        # Check boundaries
        if index < 0 or index >= self.size:
            return 
        
        # Like in addAtIndex, first find the predecessor
        predecessor = self.dummy_node
        for _ in range(index):
            predecessor = predecessor.next
        
        # The predecessor skips the node to be deleted
        predecessor.next = predecessor.next.next
        # Don't forget to decrement self.size by 1
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
```



**Complexity Analysis:**  

- *`Time Complexity`*:

  
- *`Space Complexity`*:

<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)



<h2 id = "206"><a href="https://leetcode.com/problems/reverse-linked-list">206. Reverse Linked List</a></h2><h3>Easy</h3><p>Given the <code>head</code> of a singly linked list, reverse the list, and return <em>the reversed list</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg" style="width: 542px; height: 222px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4,5]
<strong>Output:</strong> [5,4,3,2,1]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg" style="width: 182px; height: 222px;" />
<pre>
<strong>Input:</strong> head = [1,2]
<strong>Output:</strong> [2,1]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> head = []
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is the range <code>[0, 5000]</code>.</li>
	<li><code>-5000 &lt;= Node.val &lt;= 5000</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> A linked list can be reversed either iteratively or recursively. Could you implement both?</p>




### My Solution 1：_`two pointers`_  

  
```python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # two pointer 

        # 检查头节点不是空
        if not head:
            return None

        pre_node, cur_node = None, head

        while cur_node:
            #保留next节点信息
            temp = cur_node.next
            #再将current 指向 previous node
            cur_node.next = pre_node

            #pre 成为原来的cur_node
            pre_node = cur_node
            #再将保留的原next 赋给current
            cur_node = temp

        return pre_node

            
        
```


---
  

 
### My Solution 2：_`recursion`_  

  
```python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(pre_node, cur_node):
            #递归结束条件和返回值
            if not cur_node:
                # 需要返回反转的链表头部
                return pre_node

            temp_node = cur_node.next
            cur_node.next = pre_node
            
            # 单层递归逻辑
            # 需要有返回值
            return reverse(cur_node, temp_node)
        
        #递归参数
        return reverse(None, head)
```


**Complexity Analysis:**  

- *`Time Complexity`*:
O(n)
  
- *`Space Complexity`*:
O(1)
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)













