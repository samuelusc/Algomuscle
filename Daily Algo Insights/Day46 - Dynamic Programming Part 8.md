# Day46- Dynamic Programming Part 8.


## Contents
* **[139. Word Break](#139)**
* **[56. 携带矿石资源](#56)**
* **[146. LRU Cache](#146)**
<br>

<br>

<h2 id = "139"><a href="https://leetcode.com/problems/word-break">139. Word Break</a></h2><h3>Medium</h3><p>Given a string <code>s</code> and a dictionary of strings <code>wordDict</code>, return <code>true</code> if <code>s</code> can be segmented into a space-separated sequence of one or more dictionary words.</p>

<p><strong>Note</strong> that the same word in the dictionary may be reused multiple times in the segmentation.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;leetcode&quot;, wordDict = [&quot;leet&quot;,&quot;code&quot;]
<strong>Output:</strong> true
<strong>Explanation:</strong> Return true because &quot;leetcode&quot; can be segmented as &quot;leet code&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;applepenapple&quot;, wordDict = [&quot;apple&quot;,&quot;pen&quot;]
<strong>Output:</strong> true
<strong>Explanation:</strong> Return true because &quot;applepenapple&quot; can be segmented as &quot;apple pen apple&quot;.
Note that you are allowed to reuse a dictionary word.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;catsandog&quot;, wordDict = [&quot;cats&quot;,&quot;dog&quot;,&quot;sand&quot;,&quot;and&quot;,&quot;cat&quot;]
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 300</code></li>
	<li><code>1 &lt;= wordDict.length &lt;= 1000</code></li>
	<li><code>1 &lt;= wordDict[i].length &lt;= 20</code></li>
	<li><code>s</code> and <code>wordDict[i]</code> consist of only lowercase English letters.</li>
	<li>All the strings of <code>wordDict</code> are <strong>unique</strong>.</li>
</ul>
### Breakdown and Thought Process:  
<br>

### Solving approach 1:


[word break - thought](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day46/LC139-thought_1.jpg)
[word break - thought2](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day46/LC139-thought_2.jpg)




### My Solution：

  
```python

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * len(s)
        wordSet = set(wordDict)

        for i in range(1, len(s)+1):
            for j in range(i):
                word = s[j:i]

                if word in wordSet and dp[j]:
                    dp[i] = True
        
        return dp[-1]
```

**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n^2), where n is the length of string "s".
  
- *`Space Complexity`*:<br>
O(n)
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


### 56. 携带矿石资源<a name = "56"></a>
#### [Question Reference](https://kamacoder.com/problempage.php?pid=1066)

时间限制：5.000S  空间限制：256MB

### 题目描述
你是一名宇航员，即将前往一个遥远的行星。在这个行星上，有许多不同类型的矿石资源，每种矿石都有不同的重要性和价值。你需要选择哪些矿石带回地球，但你的宇航舱有一定的容量限制。 

给定一个宇航舱，最大容量为 C。现在有 N 种不同类型的矿石，每种矿石有一个重量 w[i]，一个价值 v[i]，以及最多 k[i] 个可用。不同类型的矿石在地球上的市场价值不同。你需要计算如何在不超过宇航舱容量的情况下，最大化你所能获取的总价值。

### 输入描述
输入共包括四行，第一行包含两个整数 C 和 N，分别表示宇航舱的容量和矿石的种类数量。 

接下来的三行，每行包含 N 个正整数。具体如下： 

第二行包含 N 个整数，表示 N 种矿石的重量。 

第三行包含 N 个整数，表示 N 种矿石的价格。 

第四行包含 N 个整数，表示 N 种矿石的可用数量上限。

### 输出描述
输出一个整数，代表获取的最大价值。

输入示例

10 3

1 3 4

15 20 30

2 3 2

### 输出示例
90

提示信息

数据范围：

1 <= C <= 10000;

1 <= N <= 10000;

1 <= w[i], v[i], k[i] <= 10000;

<br>

### My Solution：_`xxx`_  

  
```python


```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>

  
- *`Space Complexity`*:<br>


<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


<h2 id = "146"><a href="https://leetcode.com/problems/lru-cache">146. LRU Cache</a></h2><h3>Medium</h3><p>Design a data structure that follows the constraints of a <strong><a href="https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU" target="_blank">Least Recently Used (LRU) cache</a></strong>.</p>

<p>Implement the <code>LRUCache</code> class:</p>

<ul>
	<li><code>LRUCache(int capacity)</code> Initialize the LRU cache with <strong>positive</strong> size <code>capacity</code>.</li>
	<li><code>int get(int key)</code> Return the value of the <code>key</code> if the key exists, otherwise return <code>-1</code>.</li>
	<li><code>void put(int key, int value)</code> Update the value of the <code>key</code> if the <code>key</code> exists. Otherwise, add the <code>key-value</code> pair to the cache. If the number of keys exceeds the <code>capacity</code> from this operation, <strong>evict</strong> the least recently used key.</li>
</ul>

<p>The functions <code>get</code> and <code>put</code> must each run in <code>O(1)</code> average time complexity.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input</strong>
[&quot;LRUCache&quot;, &quot;put&quot;, &quot;put&quot;, &quot;get&quot;, &quot;put&quot;, &quot;get&quot;, &quot;put&quot;, &quot;get&quot;, &quot;get&quot;, &quot;get&quot;]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
<strong>Output</strong>
[null, null, null, 1, null, -1, null, -1, 3, 4]

<strong>Explanation</strong>
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= capacity &lt;= 3000</code></li>
	<li><code>0 &lt;= key &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= value &lt;= 10<sup>5</sup></code></li>
	<li>At most <code>2 * 10<sup>5</sup></code> calls will be made to <code>get</code> and <code>put</code>.</li>
</ul>

### Solving approach:   


![146-sol-1](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day46/LRU_1.jpg)
![146-sol-2](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day46/LRU_2.jpg)




### My Solution：_`hashmap + doubly linkedlist`_  

  
```python

class Node:
    def __init__(self, key = 0, value = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}

        self.capacity = capacity
        self.size = 0

        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head    

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.move_to_head(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            
            self.add_to_head(node)
            self.size += 1

            if self.size > self.capacity:
                removed_node = self.remove_tail()
                del self.cache[removed_node.key]
                self.size -= 1


    def move_to_head(self, node):
        self.remove_node(node)
        self.add_to_head(node)

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_to_head(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    def remove_tail(self)-> Node:
        node = self.tail.prev
        self.remove_node(node)
        return node
        # if node and node != self.head:
        #     self.remove_node(node)
        #     return node
        # else:
        #     return None


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
__init__ : O(1)
get: O(1)
put: O(1)
move_to_head: O(1)
remove_node: O(1)
add_to_head: O(1)
remove_tail: O(1)
  
- *`Space Complexity`*:<br>
O(capacity), because the cache will store at most capacity number of nodes.
