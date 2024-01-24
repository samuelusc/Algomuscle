# Day24 - Backtracking Part 1

### [Study Reference](https://programmercarl.com/%E5%9B%9E%E6%BA%AF%E7%AE%97%E6%B3%95%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html)  


## Contents
* **[77. Combinations](#77)**


## Recursion and backtracking

1. **确定递归函数的参数和返回值：**
确定哪些参数是递归的过程中需要处理的，那么就在递归函数里加上这个参数， 并且还要明确每次递归的返回值是什么进而确定递归函数的返回类型。

2. **确定终止条件：**
写完了递归算法,  运行的时候，经常会遇到栈溢出的错误，就是没写终止条件或者终止条件写的不对，操作系统也是用一个栈的结构来保存每一层递归的信息，如果递归没有终止，操作系统的内存栈必然就会溢出。

3. **确定单层递归的逻辑：**
确定每一层递归需要处理的信息。在这里也就会重复调用自己来实现递归的过程。

### Template of backtracking

```
void backtracking(参数) {
    if (终止条件) {
        存放结果;
        return;
    }

    for (选择：本层集合中元素（树中节点孩子的数量就是集合的大小）) {
        处理节点;
        backtracking(路径，选择列表); // 递归
        回溯，撤销处理结果
    }
}
```

<br>
<h2 id = "77"><a href="https://leetcode.com/problems/combinations">77. Combinations</a></h2><h3>Medium</h3><hr><p>Given two integers <code>n</code> and <code>k</code>, return <em>all possible combinations of</em> <code>k</code> <em>numbers chosen from the range</em> <code>[1, n]</code>.</p>

<p>You may return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 4, k = 2
<strong>Output:</strong> [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
<strong>Explanation:</strong> There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 1, k = 1
<strong>Output:</strong> [[1]]
<strong>Explanation:</strong> There is 1 choose 1 = 1 total combination.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 20</code></li>
	<li><code>1 &lt;= k &lt;= n</code></li>
</ul>



### My Solution 1：_`backtracking`_  

  
```python

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path, res = [], []
        def backtracking(n,k, start_index):
            if len(path) == k:
                res.append(path[:])
                return 
            

            for i in range(start_index, n - (k-len(path)) + 2):
                path.append(i)

                # 不是 start_index + 1,是当前i + 1
                backtracking(n,k, i + 1) 
                path.pop()
        
        backtracking(n,k,1)
        return res
```



**Complexity Analysis:**  

- *`Time Complexity`*:<br>
O(C(n,k)×k), C(n,k)= n!/ (k!(n−k)!). paht[:] costs O(k)
  
- *`Space Complexity`*:<br>
O(C(n,k)×k), C(n,k)= n!/ (k!(n−k)!). paht[:] costs O(k)

<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>










