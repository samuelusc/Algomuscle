# Day37 - Greedy Part5


## Contents
* **[435. Non-overlapping Intervals](#435)**
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

![Thought-process](https://github.com/samuelusc/Algomuscle/blob/main/assets/Day36/Leetcode435-thoutht.jpg)


 
### My Solution 1：_`sort + greedy`_  

  
```python

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0],x[1]))
        count = 0

        # 设定第一个比较对象
        pre_end = intervals[0][1]
        for i in range(1, len(intervals)):
            
            if intervals[i][0] < pre_end:
                count += 1
                pre_end = min(pre_end, intervals[i][1])
            # 更新 pre_end
            else:
                pre_end = intervals[i][1]

        
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




xxxxx



### My Solution 1：_`xxx`_  

  
```python


```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>

  
- *`Space Complexity`*:<br>

<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>



xxxx


### My Solution 1：_`xxx`_  

  
```python


```


**Complexity Analysis:**  

- *`Time Complexity`*:<br>

  
- *`Space Complexity`*:<br>

<br>

![Dividing Line](https://github.com/samuelusc/Algomuscle/blob/main/assets/CatDividing.png)
<br>


xxxx







