# Day06-HashMap-Part1


## Contents
* **[242. Valid Anagram](#242)**
* **[349. Intersection of Two Arrays](#349)**
* **[202. Happy Number](#202)**
* **[1. Two Sum](#1)**


<br>
<h2 id = "242"><a href="https://leetcode.com/problems/valid-anagram">242. Valid Anagram</a></h2><h3>Easy</h3><p>Given two strings <code>s</code> and <code>t</code>, return <code>true</code> <em>if</em> <code>t</code> <em>is an anagram of</em> <code>s</code><em>, and</em> <code>false</code> <em>otherwise</em>.</p>

<p>An <strong>Anagram</strong> is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<pre><strong>Input:</strong> s = "anagram", t = "nagaram"
<strong>Output:</strong> true
</pre><p><strong class="example">Example 2:</strong></p>
<pre><strong>Input:</strong> s = "rat", t = "car"
<strong>Output:</strong> false
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length, t.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>s</code> and <code>t</code> consist of lowercase English letters.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> What if the inputs contain Unicode characters? How would you adapt your solution to such a case?</p>
### Breakdown and Thought Process:  
<br>



### My Solution 1：_`Dict`_  

  
```python

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hashmap = {}

        for char in s:
            value = hashmap.get(char, 0) + 1
            hashmap[char] = value

        for char in t:
            value = hashmap.get(char, 0) - 1
            hashmap[char] = value

        return all(value == 0 for key, value in hashmap.items())
             
        
```


- *`Time Complexity`*:<br>
O(n + m), where n is the length of string s, m is the length of string t.
  
- *`Space Complexity`*:<br>
O(n + m), considering the number of unique characters in the worst case.
---
  
 
### My Solution 2：_`Easy Counter`_  

  
```python

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        s_counter = Counter(s)
        t_counter = Counter(t)

        return s_counter == t_counter
```

- *`Time Complexity`*:<br>
O(n + m), where n is the length of string s and m is the length of string t.
  
- *`Space Complexity`*:<br>
O(n + m), considering the number of unique characters in the worst case.
---


### My Solution 3：_`counter`_  

  
```python

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        # check the bundary 
        if len(s) != len(t):
            return False

        s_counter = Counter(s)

        for char in t:
            s_counter[char] -= 1
            if s_counter[char] < 0:
                return False
        
        return True

            
```

- *`Time Complexity`*:<br>
O(n + m), which simplifies to O(n) because n = m.
  
- *`Space Complexity`*:<br>
O(n), where n is the number of characters in string s.
---

### My Solution 4：

  
```python

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record = [0] * 26

        for char in s:
            record[ord(char) - ord('a')] += 1
        
        for char in t:
            record[ord(char) - ord('a')] -= 1

        for num in record:
            if num:
                return False

        return True
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n + m) since 26 is a constant and does not scale with the input.
  
- *`Space Complexity`*:<br>
O(1), as it only requires a fixed amount of space.

<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


<h2 id = "349"><a href="https://leetcode.com/problems/intersection-of-two-arrays">349. Intersection of Two Arrays</a></h2><h3>Easy</h3><p>Given two integer arrays <code>nums1</code> and <code>nums2</code>, return <em>an array of their intersection</em>. Each element in the result must be <strong>unique</strong> and you may return the result in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,2,2,1], nums2 = [2,2]
<strong>Output:</strong> [2]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [4,9,5], nums2 = [9,4,9,8,4]
<strong>Output:</strong> [9,4]
<strong>Explanation:</strong> [4,9] is also accepted.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums1.length, nums2.length &lt;= 1000</code></li>
	<li><code>0 &lt;= nums1[i], nums2[i] &lt;= 1000</code></li>
</ul>





### My Solution 1：_`Dict`_  

  
```python

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashTable = dict()
        res = set()
        for num in nums1:
            
            hashTable[num] = hashTable.get(num, 0) + 1

        for num in nums2:
            if num in hashTable:
                res.add(num)

        return list(res)
                
```


- *`Time Complexity`*:<br>
O(n + m + k), which in the worst case can be O(n + m)
  
- *`Space Complexity`*:<br>
O(n + min(n, m)), which can be simplified to O(n), assuming n is the size of the larger array.
---
  

### My Solution 2：_`set`_  

  
```python

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # create a set copy of nums1 and nums2
        # find the intersection by & operator
        return list(set(nums1) & set(nums2))
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n + m + min(n, m)), which simplifies to O(n + m) assuming the set intersection operation is not the dominant factor.
  
- *`Space Complexity`*:<br>
O(n + m), where n and m are the lengths of nums1 and nums2, respectively.
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


<h2 id = "202"><a href="https://leetcode.com/problems/happy-number">202. Happy Number</a></h2><h3>Easy</h3><p>Write an algorithm to determine if a number <code>n</code> is happy.</p>

<p>A <strong>happy number</strong> is a number defined by the following process:</p>

<ul>
	<li>Starting with any positive integer, replace the number by the sum of the squares of its digits.</li>
	<li>Repeat the process until the number equals 1 (where it will stay), or it <strong>loops endlessly in a cycle</strong> which does not include 1.</li>
	<li>Those numbers for which this process <strong>ends in 1</strong> are happy.</li>
</ul>

<p>Return <code>true</code> <em>if</em> <code>n</code> <em>is a happy number, and</em> <code>false</code> <em>if not</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 19
<strong>Output:</strong> true
<strong>Explanation:</strong>
1<sup>2</sup> + 9<sup>2</sup> = 82
8<sup>2</sup> + 2<sup>2</sup> = 68
6<sup>2</sup> + 8<sup>2</sup> = 100
1<sup>2</sup> + 0<sup>2</sup> + 0<sup>2</sup> = 1
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 2<sup>31</sup> - 1</code></li>
</ul>




### My Solution 1：_`set`_  

  
```python

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n!= 1:
            # calculate by list comprehension
            n = sum(int(i) ** 2 for i in str(n))
            # check if it is in hash table 
            if n in seen:
                return False
            else:
                seen.add(n)
        # if n == 1
        return True
```


- *`Time Complexity`*:<br>
O(d) where d is the number of digits in n
  
- *`Space Complexity`*:<br>
O(k), where k is the number of unique numbers generated by the sum of squares of the digits process. 
---
  

 
### My Solution 2：_`twoPointers`_  

  
```python

class Solution:
    def isHappy(self, n: int) -> bool:
        def next_number(num):
            total_sum = 0
            # or we can use sum(int(digit) ** 2 for digit in str(num))
            while num:
                num, remainder = divmod(num, 10)
                total_sum += remainder ** 2
            return total_sum

        slow = n
        fast = next_number(n)
        # tend to make mistake to set next_number(n)
        while slow != fast:
            slow = next_number(slow)
            fast = next_number(next_number(fast))

        return slow == 1
            
```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(d) where d is the number of digits in n
  
- *`Space Complexity`*:<br>
O(1), as it does not require space that scales with the size of the input.
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


<h2 id = "01"><a href="https://leetcode.com/problems/two-sum">1. Two Sum</a></h2><h3>Easy</h3><p>Given an array of integers <code>nums</code>&nbsp;and an integer <code>target</code>, return <em>indices of the two numbers such that they add up to <code>target</code></em>.</p>

<p>You may assume that each input would have <strong><em>exactly</em> one solution</strong>, and you may not use the <em>same</em> element twice.</p>

<p>You can return the answer in any order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,7,11,15], target = 9
<strong>Output:</strong> [0,1]
<strong>Explanation:</strong> Because nums[0] + nums[1] == 9, we return [0, 1].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,4], target = 6
<strong>Output:</strong> [1,2]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,3], target = 6
<strong>Output:</strong> [0,1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li>
	<li><strong>Only one valid answer exists.</strong></li>
</ul>

<p>&nbsp;</p>
<strong>Follow-up:&nbsp;</strong>Can you come up with an algorithm that is less than <code>O(n<sup>2</sup>)</code><font face="monospace">&nbsp;</font>time complexity?




### My Solution 1：_`dict`_  

  
```python

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        # enumerate throught the list of numbers
        for index, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], index]
            
            seen[num] = index

```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(n), where n is the number of elements in nums.  
- *`Space Complexity`*:<br>
O(n), proportional to the number of elements in the list.
<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>

