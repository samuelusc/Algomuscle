class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 先映射进一个列表, 不包括 0，1
        letterMap = ["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]


        # 如果digits is ""
        if not digits:
            return []
        
        # 最终返回表
        res = ['']

        for digit in digits:
            #! 最开始写成了 digits 错误
            letters = letterMap[int(digit) -2 ]
            # first iteration res = ["a","b""c"] if digits = "23"
            res = [prefix + char for prefix in res for char in letters]

        return res