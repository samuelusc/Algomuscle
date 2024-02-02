# Day35 - Greedy Part4


## Contents
* **[860. Lemonade Change](#860)**
* **[406.Queue Reconstruction by Height](#406)**
* **[452. Minimum Number of Arrows to Burst Balloons](#452)**
* **[9. Palindrome Number](#9)**

<br>
<h2 id = "860"><a href="https://leetcode.com/problems/lemonade-change">860. Lemonade Change</a></h2><h3>Easy</h3><hr><p>At a lemonade stand, each lemonade costs <code>$5</code>. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a <code>$5</code>, <code>$10</code>, or <code>$20</code> bill. You must provide the correct change to each customer so that the net transaction is that the customer pays <code>$5</code>.</p>

<p>Note that you do not have any change in hand at first.</p>

<p>Given an integer array <code>bills</code> where <code>bills[i]</code> is the bill the <code>i<sup>th</sup></code> customer pays, return <code>true</code> <em>if you can provide every customer with the correct change, or</em> <code>false</code> <em>otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> bills = [5,5,5,10,20]
<strong>Output:</strong> true
<strong>Explanation:</strong> 
From the first 3 customers, we collect three $5 bills in order.
From the fourth customer, we collect a $10 bill and give back a $5.
From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change, we output true.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> bills = [5,5,10,10,20]
<strong>Output:</strong> false
<strong>Explanation:</strong> 
From the first two customers in order, we collect two $5 bills.
For the next two customers in order, we collect a $10 bill and give back a $5 bill.
For the last customer, we can not give the change of $15 back because we only have two $10 bills.
Since not every customer received the correct change, the answer is false.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= bills.length &lt;= 10<sup>5</sup></code></li>
	<li><code>bills[i]</code> is either <code>5</code>, <code>10</code>, or <code>20</code>.</li>
</ul>
### Breakdown and Thought Process:  
<br>

### Solving approach 1:


xxxx


### My Solution 1：_`greedy`_  

  
```python

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0,0 
        for bill in bills:
            if bill == 5:
                five += 1

            elif bill == 10:
                if not five:
                    return False
                five -= 1
                ten += 1
            
            # 在20情况下，要优先使用10+5 其次5*3
            else:
                if ten and five:
                    ten -= 1
                    five -= 1
                
                elif five > 2:
                    five -= 3

                else:
                    return False
        return True
```



**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n), where n is the number of bills.
  
- *`Space Complexity`*:<br>
O(1)
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


<h2 id = "406"><a href="https://leetcode.com/problems/queue-reconstruction-by-height">406. Queue Reconstruction by Height</a></h2><h3>Medium</h3><hr><p>You are given an array of people, <code>people</code>, which are the attributes of some people in a queue (not necessarily in order). Each <code>people[i] = [h<sub>i</sub>, k<sub>i</sub>]</code> represents the <code>i<sup>th</sup></code> person of height <code>h<sub>i</sub></code> with <strong>exactly</strong> <code>k<sub>i</sub></code> other people in front who have a height greater than or equal to <code>h<sub>i</sub></code>.</p>

<p>Reconstruct and return <em>the queue that is represented by the input array </em><code>people</code>. The returned queue should be formatted as an array <code>queue</code>, where <code>queue[j] = [h<sub>j</sub>, k<sub>j</sub>]</code> is the attributes of the <code>j<sup>th</sup></code> person in the queue (<code>queue[0]</code> is the person at the front of the queue).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
<strong>Output:</strong> [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
<strong>Explanation:</strong>
Person 0 has height 5 with no other people taller or the same height in front.
Person 1 has height 7 with no other people taller or the same height in front.
Person 2 has height 5 with two persons taller or the same height in front, which is person 0 and 1.
Person 3 has height 6 with one person taller or the same height in front, which is person 1.
Person 4 has height 4 with four people taller or the same height in front, which are people 0, 1, 2, and 3.
Person 5 has height 7 with one person taller or the same height in front, which is person 1.
Hence [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] is the reconstructed queue.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
<strong>Output:</strong> [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= people.length &lt;= 2000</code></li>
	<li><code>0 &lt;= h<sub>i</sub> &lt;= 10<sup>6</sup></code></li>
	<li><code>0 &lt;= k<sub>i</sub> &lt; people.length</code></li>
	<li>It is guaranteed that the queue can be reconstructed.</li>
</ul>

### Solving approach 1:



1. `先按照身高降序排列`。sort(key = len) 是in place modify original list。Parameter key 是可选的，如果不写为升序排列。 sort()只能用在列表，sorted(iterable, key = len/reverse = True)可以用在其他可迭代对象如tuple,dict.


2.  `people.sort(key = lambda x: (-x[0],x[1])`。 x 就是 people中的元素，即为[h,k]，它返回一个tuple(-x[0],x[1]), 这里 -x[0]表示按照降序排列，当第一个元素相同时会按第二个元素x[1]升序排。
   
   
   - `lambda arguments: expression`


```python
# Case 1 
add = lambda x, y: x + y
print(add(5, 3))  # 输出: 8

# 相当于
def add(x, y):
    return x + y

print(add(5, 3))  # 输出: 8

# Case 2 综合排序
points = [(1, 2), (3, 3), (5, 1)]
points.sort(key=lambda x: x[1])
print(points)  # 输出: [(5, 1), (1, 2), (3, 3)]

# Case3 map(), filter() 结合使用
nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, nums))
print(squared)  # 输出: [1, 4, 9, 16, 25]

even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)  # 输出: [2, 4]


```


4.  insert() 方法只用在列表，

  
```python
my_list = [1, 2, 3, 4, 5]

my_list.insert(2, 'X')  # 在索引位置 2 之前插入 'X'
# 现在列表变为 [1, 2, 'X', 3, 4, 5]

my_list.insert(-1, 'Y')  # 在倒数第一个位置（最后一个位置）之后插入 'Y'
# 现在列表变为 [1, 2, 'X', 3, 4, 'Y', 5]


```


### My Solution 1：_`xxx`_  

  
```python

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        #先满足height 然后满足k
        # 排序 
        people.sort(key = lambda x: (-x[0],x[1]))

        queue = []

        for each in people:
            # 将 each 按照k的位置插入
            queue.insert(each[1], each)

        return queue
```



**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n^2), where n is the number of people. Sorting opertion in PYthon is O(nlogn).

  
- *`Space Complexity`*:<br>
O(n)

<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>



<h2 id = "452"><a href="https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons">452. Minimum Number of Arrows to Burst Balloons</a></h2><h3>Medium</h3><hr><p>There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array <code>points</code> where <code>points[i] = [x<sub>start</sub>, x<sub>end</sub>]</code> denotes a balloon whose <strong>horizontal diameter</strong> stretches between <code>x<sub>start</sub></code> and <code>x<sub>end</sub></code>. You do not know the exact y-coordinates of the balloons.</p>

<p>Arrows can be shot up <strong>directly vertically</strong> (in the positive y-direction) from different points along the x-axis. A balloon with <code>x<sub>start</sub></code> and <code>x<sub>end</sub></code> is <strong>burst</strong> by an arrow shot at <code>x</code> if <code>x<sub>start</sub> &lt;= x &lt;= x<sub>end</sub></code>. There is <strong>no limit</strong> to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.</p>

<p>Given the array <code>points</code>, return <em>the <strong>minimum</strong> number of arrows that must be shot to burst all balloons</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> points = [[10,16],[2,8],[1,6],[7,12]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> points = [[1,2],[3,4],[5,6],[7,8]]
<strong>Output:</strong> 4
<strong>Explanation:</strong> One arrow needs to be shot for each balloon for a total of 4 arrows.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> points = [[1,2],[2,3],[3,4],[4,5]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
- Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= points.length &lt;= 10<sup>5</sup></code></li>
	<li><code>points[i].length == 2</code></li>
	<li><code>-2<sup>31</sup> &lt;= x<sub>start</sub> &lt; x<sub>end</sub> &lt;= 2<sup>31</sup> - 1</code></li>
</ul><br>


### My Solution 1：_`xxx`_  

  
```python

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort(key = lambda x: (x[0],x[1]))
        # 对于第一个或第一组重叠气球至少需要一箭
        count = 1

        for i in range(len(points)-1):
            if points[i][1] < points[i + 1][0]:
                count += 1
            
            else:
                points[i+1][1] = min(points[i][1], points[i+1][1])

        
        return count

```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(nlogn)
  
- *`Space Complexity`*:<br>
O(1)
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


<h2 id = "9"><a href="https://leetcode.com/problems/palindrome-number">9. Palindrome Number</a></h2><h3>Easy</h3><hr><p>Given an integer <code>x</code>, return <code>true</code><em> if </em><code>x</code><em> is a </em><span data-keyword="palindrome-integer"><em><strong>palindrome</strong></em></span><em>, and </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> x = 121
<strong>Output:</strong> true
<strong>Explanation:</strong> 121 reads as 121 from left to right and from right to left.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> x = -121
<strong>Output:</strong> false
<strong>Explanation:</strong> From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> x = 10
<strong>Output:</strong> false
<strong>Explanation:</strong> Reads 01 from right to left. Therefore it is not a palindrome.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-2<sup>31</sup>&nbsp;&lt;= x &lt;= 2<sup>31</sup>&nbsp;- 1</code></li>
</ul>

<p>&nbsp;</p>
<strong>Follow up:</strong> Could you solve it without converting the integer to a string?
### My Solution 1：_`xxx`_  

  
```python

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x and x % 10 == 0):
            return False

        half = 0

        while half < x:
            half = half * 10 + x % 10
            x = x // 10

        return x in (half, half // 10)
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(log n)
  
- *`Space Complexity`*:<br>
O(1)
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>









