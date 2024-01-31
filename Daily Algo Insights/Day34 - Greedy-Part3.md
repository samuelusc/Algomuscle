# Day34 - Greedy Part3

### [Study Reference](https://programmercarl.com/0020.%E6%9C%89%E6%95%88%E7%9A%84%E6%8B%AC%E5%8F%B7.html)  

## Contents
* **[xx](#xxx)**
* **[xx](#)**
* **[xx](#)**
* **[xx](#)**
* **[xx](#)**
<br>
xxximagexxx
<br>
xxxx Question Description with id="xxx"

### Breakdown and Thought Process:  
<br>

### Solving approach 1:


xxxx


### My Solution 1：_`xxx`_  

  
```python


```


- *`Time Complexity`*:<br>

  
- *`Space Complexity`*:<br>
---
  
### Solving approach 2:  


xxx

 
### My Solution 2：_`xxx`_  

  
```python


```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>

  
- *`Space Complexity`*:<br>

<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


xxxx Question Description with id="xxx"


### Solving approach 1:


1. 先按照身高降序排列。sort(key = len) 是in place modify original list。Parameter key 是可选的，如果不写为升序排列。 

2.  people.sort(key = lambda x: (-x[0],x[1])。 x 就是 people中的元素，即为[h,k]，它返回一个tuple(-x[0],x[1]), 这里 -x[0]表示按照降序排列，当第一个元素相同时会按第二个元素x[1]升序排。
   
   - lambda arguments: expression

```python
# Case 1 
add = lambda x, y: x + y
print(add(5, 3))  # 输出: 8

# 相当于
def add(x, y):
    return x + y

print(add(5, 3))  # 输出: 8

# 综合排序
points = [(1, 2), (3, 3), (5, 1)]
points.sort(key=lambda x: x[1])
print(points)  # 输出: [(5, 1), (1, 2), (3, 3)]

# map(), filter() 结合使用
nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, nums))
print(squared)  # 输出: [1, 4, 9, 16, 25]

even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)  # 输出: [2, 4]


```

4.  

### My Solution 1：_`xxx`_  

  
```python


```


- *`Time Complexity`*:<br>

  
- *`Space Complexity`*:<br>
---
  
### Solving approach 2:  


xxx

 
### My Solution 2：_`xxx`_  

  
```python


```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>

  
- *`Space Complexity`*:<br>

<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


xxxx Question Description with id="xxx"

### Breakdown and Thought Process:  
<br>

### Solving approach 1:


xxxx


### My Solution 1：_`xxx`_  

  
```python


```


- *`Time Complexity`*:<br>

  
- *`Space Complexity`*:<br>
---
  
### Solving approach 2:  


xxx

 
### My Solution 2：_`xxx`_  

  
```python


```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>

  
- *`Space Complexity`*:<br>

<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>












