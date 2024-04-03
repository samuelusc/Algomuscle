# Day04-LinkedList-Part2


## Contents
* **[24. Swap Nodes in Pairs](#24)**
* **[19. Remove Nth Node From End of List](#19)**
* **[160. Intersection of Two Linked Lists](#160)**
* **[142. Linked List Cycle II](#142)**

<br>
<h2 id = "24"><a href="https://leetcode.com/problems/swap-nodes-in-pairs">24. Swap Nodes in Pairs</a></h2><h3>Medium</h3><p>Given a&nbsp;linked list, swap every two adjacent nodes and return its head. You must solve the problem without&nbsp;modifying the values in the list&#39;s nodes (i.e., only nodes themselves may be changed.)</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/swap_ex1.jpg" style="width: 422px; height: 222px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4]
<strong>Output:</strong> [2,1,4,3]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> head = []
<strong>Output:</strong> []
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> head = [1]
<strong>Output:</strong> [1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the&nbsp;list&nbsp;is in the range <code>[0, 100]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 100</code></li>
</ul>
### Breakdown and Thought Process:  
<br>



### My Solution 1：_`Recursion`_  

  
```python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Check for edge cases and establish the base case for recursion
        if not head or not head.next:
            return head

        new_head = head.next
        head.next = self.swapPairs(new_head.next)
        
        # Connect the new head node to the original head
        new_head.next = head
        
        # Return the new head (both for recursion backtracking and as the final output)
        return new_head
```


- *`Time Complexity`*:<br>
O(n), where n is the total number of nodes in the list.
  
- *`Space Complexity`*:<br>
O(n), where n is the number of nodes in the list.
---
  

 
### My Solution 2：_`Stack version`_  

  
```python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Check for boundary conditions: only one node or no nodes
        if not head or not head.next:
            return head
        dummy_node = ListNode(next = head)

        # cur_node to give the next pair's start
        # pre_node as the predecessor of the next head node
        cur_node, pre_node, stack = head, dummy_node, []

        # Need to consider two nodes at a time, so must include current node and current next node
        while cur_node and cur_node.next:
            
            _,_ = stack.append(cur_node),stack.append(cur_node.next)
            # Head of the next pair of nodes
            cur_node = cur_node.next.next

            # Use the stack's characteristics to sequentially connect to the dummy node
            pre_node.next = stack.pop()
            pre_node.next.next = stack.pop()

            # Move forward to the node that has been swapped, the node before the one to be added
            pre_node = pre_node.next.next
        
        # If the number of nodes is odd, connect the previous node with the remaining single node
        pre_node.next = cur_node if cur_node else None

        return dummy_node.next
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n), where n is the total number of nodes in the list.
  
- *`Space Complexity`*:<br>
 O(1)
---


### My Solution 3：

  
```python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        #将curret 指着 dummy
        cur_node = dummy
        
        #两两交换，至少要往前2次
        while cur_node.next and cur_node.next.next:
            #首先保存 第一个节点
            first_node = cur_node.next
            #保存第二个节点
            second_node = cur_node.next.next
           
            #将虚拟节点的下一个指向 第二个节点
            cur_node.next = second_node
            
            #将节点1的下一个指向节点2的下一个(1->3)
            first_node.next = second_node.next
            #将第节点2的下一个指向节点1（注意这里和上一个的顺序）
            second_node.next = first_node

            #把current指针移动到交换后的节点1
            cur_node = first_node
        
        return dummy.next
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n), where n is the total number of nodes in the list.
  
- *`Space Complexity`*:<br>
O(1), as it only requires a constant amount of space beyond the input list.
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


<h2 id = "19"><a href="https://leetcode.com/problems/remove-nth-node-from-end-of-list">19. Remove Nth Node From End of List</a></h2><h3>Medium</h3><p>Given the <code>head</code> of a linked list, remove the <code>n<sup>th</sup></code> node from the end of the list and return its head.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg" style="width: 542px; height: 222px;" />
<pre>
<strong>Input:</strong> head = [1,2,3,4,5], n = 2
<strong>Output:</strong> [1,2,3,5]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> head = [1], n = 1
<strong>Output:</strong> []
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> head = [1,2], n = 1
<strong>Output:</strong> [1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is <code>sz</code>.</li>
	<li><code>1 &lt;= sz &lt;= 30</code></li>
	<li><code>0 &lt;= Node.val &lt;= 100</code></li>
	<li><code>1 &lt;= n &lt;= sz</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you do this in one pass?</p>




### My Solution:

  
```python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy_node = ListNode(next = head)
        fast = slow = dummy_node
        
        # Move the fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next
        
        # Traverse with the fast pointer until the end
        # The slow pointer will reach the node just before the nth node from the end
        while fast.next:
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
        return dummy_node.next
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n), where n is the total number of nodes in the list (not to be confused with the input parameter n).
  
- *`Space Complexity`*:<br>
O(1), as it requires a constant amount of space beyond the input list.
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>




<h2 id = "160"><a href="https://leetcode.com/problems/intersection-of-two-linked-lists">160. Intersection of Two Linked Lists</a></h2><h3>Easy</h3><p>Given the heads of two singly linked-lists <code>headA</code> and <code>headB</code>, return <em>the node at which the two lists intersect</em>. If the two linked lists have no intersection at all, return <code>null</code>.</p>

<p>For example, the following two linked lists begin to intersect at node <code>c1</code>:</p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/05/160_statement.png" style="width: 500px; height: 162px;" />
<p>The test cases are generated such that there are no cycles anywhere in the entire linked structure.</p>

<p><strong>Note</strong> that the linked lists must <strong>retain their original structure</strong> after the function returns.</p>

<p><strong>Custom Judge:</strong></p>

<p>The inputs to the <strong>judge</strong> are given as follows (your program is <strong>not</strong> given these inputs):</p>

<ul>
	<li><code>intersectVal</code> - The value of the node where the intersection occurs. This is <code>0</code> if there is no intersected node.</li>
	<li><code>listA</code> - The first linked list.</li>
	<li><code>listB</code> - The second linked list.</li>
	<li><code>skipA</code> - The number of nodes to skip ahead in <code>listA</code> (starting from the head) to get to the intersected node.</li>
	<li><code>skipB</code> - The number of nodes to skip ahead in <code>listB</code> (starting from the head) to get to the intersected node.</li>
</ul>

<p>The judge will then create the linked structure based on these inputs and pass the two heads, <code>headA</code> and <code>headB</code> to your program. If you correctly return the intersected node, then your solution will be <strong>accepted</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/05/160_example_1_1.png" style="width: 500px; height: 162px;" />
<pre>
<strong>Input:</strong> intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
<strong>Output:</strong> Intersected at &#39;8&#39;
<strong>Explanation:</strong> The intersected node&#39;s value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
- Note that the intersected node&#39;s value is not 1 because the nodes with value 1 in A and B (2<sup>nd</sup> node in A and 3<sup>rd</sup> node in B) are different node references. In other words, they point to two different locations in memory, while the nodes with value 8 in A and B (3<sup>rd</sup> node in A and 4<sup>th</sup> node in B) point to the same location in memory.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/05/160_example_2.png" style="width: 500px; height: 194px;" />
<pre>
<strong>Input:</strong> intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
<strong>Output:</strong> Intersected at &#39;2&#39;
<strong>Explanation:</strong> The intersected node&#39;s value is 2 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/05/160_example_3.png" style="width: 300px; height: 189px;" />
<pre>
<strong>Input:</strong> intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
<strong>Output:</strong> No intersection
<strong>Explanation:</strong> From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes of <code>listA</code> is in the <code>m</code>.</li>
	<li>The number of nodes of <code>listB</code> is in the <code>n</code>.</li>
	<li><code>1 &lt;= m, n &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= skipA &lt;&nbsp;m</code></li>
	<li><code>0 &lt;= skipB &lt;&nbsp;n</code></li>
	<li><code>intersectVal</code> is <code>0</code> if <code>listA</code> and <code>listB</code> do not intersect.</li>
	<li><code>intersectVal == listA[skipA] == listB[skipB]</code> if <code>listA</code> and <code>listB</code> intersect.</li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you write a solution that runs in <code>O(m + n)</code> time and use only <code>O(1)</code> memory?



### My Solution 1：_`twoPointers`_  

  
```python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # a + b = b+a
        currentA, currentB = headA, headB

        while currentA != currentB:
            # It's crucial to understand why we can't use if currentA.next here
            # Using if currentA.next won't allow entering None, causing an infinite loop
            currentA = currentA.next if currentA else headB
            currentB = currentB.next if currentB else headA
        
        return currentA
 
```


- *`Time Complexity`*:<br>
O(n + m), where n and m are the lengths of lists A and B, respectively.
  
- *`Space Complexity`*:<br>
O(1), as the algorithm only requires a constant amount of extra space regardless of the size of the input lists.
---

### My Solution 2：_`HashTable`_  

  
```python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited_nodes = set()
        cur_node = headA

        while cur_node:
            visited_nodes.add(cur_node)
            cur_node = cur_node.next

        cur_node = headB
        
        while cur_node:
            if cur_node in visited_nodes:
                return cur_node
            
            cur_node = cur_node.next
        
        return None

```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n + m), where n and m are the lengths of lists A and B, respectively.
  
- *`Space Complexity`*:<br>
O(n), where n is the number of nodes in list A.
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


<h2 id = "142"><a href="https://leetcode.com/problems/linked-list-cycle-ii">142. Linked List Cycle II</a></h2><h3>Medium</h3><p>Given the <code>head</code> of a linked list, return <em>the node where the cycle begins. If there is no cycle, return </em><code>null</code>.</p>

<p>There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the <code>next</code> pointer. Internally, <code>pos</code> is used to denote the index of the node that tail&#39;s <code>next</code> pointer is connected to (<strong>0-indexed</strong>). It is <code>-1</code> if there is no cycle. <strong>Note that</strong> <code>pos</code> <strong>is not passed as a parameter</strong>.</p>

<p><strong>Do not modify</strong> the linked list.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png" style="height: 145px; width: 450px;" />
<pre>
<strong>Input:</strong> head = [3,2,0,-4], pos = 1
<strong>Output:</strong> tail connects to node index 1
<strong>Explanation:</strong> There is a cycle in the linked list, where tail connects to the second node.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png" style="height: 105px; width: 201px;" />
<pre>
<strong>Input:</strong> head = [1,2], pos = 0
<strong>Output:</strong> tail connects to node index 0
<strong>Explanation:</strong> There is a cycle in the linked list, where tail connects to the first node.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png" style="height: 65px; width: 65px;" />
<pre>
<strong>Input:</strong> head = [1], pos = -1
<strong>Output:</strong> no cycle
<strong>Explanation:</strong> There is no cycle in the linked list.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of the nodes in the list is in the range <code>[0, 10<sup>4</sup>]</code>.</li>
	<li><code>-10<sup>5</sup> &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
	<li><code>pos</code> is <code>-1</code> or a <strong>valid index</strong> in the linked-list.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Can you solve it using <code>O(1)</code> (i.e. constant) memory?</p>



### My Solution 1：_`Set`_  

  
```python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Utilize a set to detect a cycle.
        # Sets can contain any hashable object, and ListNode can be inserted into a set.
        visited_nodes = set()

        # Traverse the linked list.
        while head:
            # If the node is already in the set, return it as the cycle's start node.
            if head in visited_nodes:
                return head
            # Add the current node to the set and move to the next node.
            visited_nodes.add(head)
            head = head.next
        # If no cycle is found, return None after complete traversal.
        return None
```


- *`Time Complexity`*:<br>
O(n), where n is the number of nodes in the linked list.
  
- *`Space Complexity`*:<br>
O(n), where n is the number of nodes in the linked list.
---
  

 
### My Solution 2：_`Twopointers`_  

  
```python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize two pointers for the two-pointer technique.
        slow = fast = head
        # Move the fast pointer two steps and the slow pointer one step. 
        # If there's a cycle, they will meet.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # Once they meet, set another pointer at the start.
            if slow == fast:
                start = head
                # This pointer will meet the slow pointer at the start of the cycle.
                while start != slow:
                    start = start.next
                    slow = slow.next
                return start  # Cycle's entry point
        
        return None  # No cycle found
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n), where n is the number of nodes in the list.
  
- *`Space Complexity`*:<br>
O(1), as the algorithm only requires a constant amount of space.
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


