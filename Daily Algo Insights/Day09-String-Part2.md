# Day09 - String Part 2

## Contents
* [28. Find the Index of the First Occurrence in a String](#28)
* [459. Repeated Substring Pattern](#459)
* [268. Smallest Missing Integer](#268)
* [xx](#)
* [xx](#)


<h2 id="28"><a href="https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string">28. Find the Index of the First Occurrence in a String</a></h2><h3>Easy</h3><hr><p>Given two strings <code>needle</code> and <code>haystack</code>, return the index of the first occurrence of <code>needle</code> in <code>haystack</code>, or <code>-1</code> if <code>needle</code> is not part of <code>haystack</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> haystack = &quot;sadbutsad&quot;, needle = &quot;sad&quot;
<strong>Output:</strong> 0
<strong>Explanation:</strong> &quot;sad&quot; occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> haystack = &quot;leetcode&quot;, needle = &quot;leeto&quot;
<strong>Output:</strong> -1
<strong>Explanation:</strong> &quot;leeto&quot; did not occur in &quot;leetcode&quot;, so we return -1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= haystack.length, needle.length &lt;= 10<sup>4</sup></code></li>
	<li><code>haystack</code> and <code>needle</code> consist of only lowercase English characters.</li>
</ul>

### Solving approach:


#### My Solution 1：_`for + slicing`_
```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Slicing approach

        h_len, n_len = len(haystack), len(needle)

        if h_len < n_len:
            return -1
        
        for i in range(0, h_len - n_len + 1):
            if haystack[i: i + n_len] == needle:
                return i
        
        return -1

	# return haystack.find(needle) 
	# if find needle ,will return start index in haystack or return  - 1 if can't it.
	# string.find(substring, start, end) optional: (start, end)
```

- *`Time Complexity`*:
O((n-m+1) * m) -> O(n*m)
- *`Space Complexity`*:
O(1)
### Solving approach:

#### My Solution 2：_`two pointers(for+while)`_
```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h_len,n_len = len(haystack), len(needle)
        
        # boundary check
        if h_len < n_len:
            return -1
        # iterate through haystack 
        for i in range(0,h_len - n_len + 1):
            
            left,right = i, 0

            # if the letter of haystack is the same as needle
            if haystack[left] == needle[right]:
                while right < n_len:
                                       
                    if haystack[left] != needle[right]:
                        break
                    if right == n_len-1:
                        return i

                    left += 1
                    right += 1
        return -1

```

**Complexity Analysis:**

- *`Time Complexity`*:
O((n-m+1) * m) -> O(n*m)
- *`Space Complexity`*:
O(1)

<h2 id ="459"><a href="https://leetcode.com/problems/repeated-substring-pattern">459. Repeated Substring Pattern</a></h2><h3>Easy</h3><hr><p>Given a string <code>s</code>, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abab&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> It is the substring &quot;ab&quot; twice.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aba&quot;
<strong>Output:</strong> false
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcabcabcabc&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> It is the substring &quot;abc&quot; four times or the substring &quot;abcabc&quot; twice.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
</ul>

#### Solving approach:
- 可以利用 **`字符串的重复性质`** 来检测是否's'可以由它的子字符重复多次构成。如果's'确实可以由其字符串重复构成，那么在2s中找到完全匹配s的初始位置将在第一个s结束前也就是index<len(s).</br>

- 检查 len(s) <= 1，return False(避免了空集index问题）

#### My Solution 1：_`2S`_
```python

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
         # create 2s
         if len(s) <= 1:
	     return False

         double_s = s + s
         index_s = double_s.index(s, 1)

         return index_s < len(s)
         

```

- *`Time Complexity`*:
O(n^2)
- *`Space Complexity`*:
O(n)

<h2 id="268"><a href="https://leetcode.com/problems/missing-number">268. Missing Number</a></h2><h3>Easy</h3><hr><p>Given an array <code>nums</code> containing <code>n</code> distinct numbers in the range <code>[0, n]</code>, return <em>the only number in the range that is missing from the array.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,0,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong> n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong> n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [9,6,4,2,3,5,7,0,1]
<strong>Output:</strong> 8
<strong>Explanation:</strong> n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= n</code></li>
	<li>All the numbers of <code>nums</code> are <strong>unique</strong>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you implement a solution using only <code>O(1)</code> extra space complexity and <code>O(n)</code> runtime complexity?</p>

#### Solving approach:
- 要想一下，如果从0开始的数组，它所缺失的最小数必然与按自然数循环的i 不同，那么i 就是缺失的那个。否则就是len(nums)
- 本题用了sort直接改变了数组也可以用sorted(nums) 创建一个新数组

#### My Solution 1：_`Sort`_
```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        
        return len(nums)

```

- *`Time Complexity`*:
O(nlogn)
- *`Space Complexity`*:
O(1)

#### Solving approach:
- 需要处理 follow up question: 如何降低复杂度到O(n) 并维持O(1) in place 空间
- 采用 ***`in-place hashing`*** , 非数据结构所称的hashing  data structure， 而是利用 **`数组索引作为key`** 存储和检索值的技术。这种方将数组自身用作哈希表，其中元素值和数组索引有直接关系。
- Don't forget to check nums[i] < n boundary check, 防止 nums[nums[i]] 越界

#### My Solution 2：_`in_place hashing`_
```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)

        for i in range(len(nums)):
            while nums[i]<n and nums[i]!= nums[nums[i]]:
                #should consider why to apply this order instead of 
                # nums[i],nums[nums[i]]
                nums[nums[i]],nums[i] = nums[i], nums[nums[i]]

        for i in range(len(nums)):
            if i != nums[i]:
                return i
        
        return len(nums)

```

**Complexity Analysis:**

- *`Time Complexity`*:
O(n) where n represents the size of the input. Each element in the array is swapped at most once into its correct position. Once an element is in the correct position, it won't be moved again.
- *`Space Complexity`*:
O(1)
