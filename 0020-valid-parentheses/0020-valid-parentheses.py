class Solution:
    def isValid(self, s: str) -> bool:
        # 设置每对字符串作为set元素
        hashset = {'()','{}','[]'}
        stack = []

        #遇到左括号的情况
        #遇到右括号的情况（stack中无左括号，stack中左括号和右括号不相匹配）
        for char in s:
            # 把这三类左括号当成迭代对象去确认，中间无逗号。放入stack            
            if char in '({[':
                stack.append(char)
            # 1 stack 为空 2. 左右不匹配 则返回 False
            elif not stack or stack.pop() + char not in hashset:
                return False
        
        # 如果stack 空，则返回True
        return not stack