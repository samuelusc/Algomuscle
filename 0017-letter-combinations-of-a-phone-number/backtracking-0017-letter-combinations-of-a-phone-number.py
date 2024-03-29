class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letterMap = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        result = []
        combo = '' # 套函数如果需要修改要么1.作为参数传递 2. 用nonlocal 字段在套函数内声明
        if not digits:
            return []

        def backtracking(combo, index):
            
            
            # base case 终止条件
            if index == len(digits):
                result.append(combo)
                return
            
            digit = int(digits[index] )
            letters = letterMap[digit]

            for char in letters:

                backtracking(combo + char, index + 1) # 这里实现了回溯
                # combo = combo[:-1] 这部分导致错误，每次调用会产生新的combo副本
        # 先定义后调用
        backtracking(combo, 0)
        return result
            


            
