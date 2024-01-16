class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        from collections import Counter
        # 创建一个计数器来计算赎金信中每个字符的出现次数
        hash_table = Counter(ransomNote)
        
        # 遍历杂志中的每个字符
        for i in magazine:
           
            # 如果字符存在于赎金信计数器中，则减少相应字符的计数
            if i in hash_table:
                hash_table[i] -= 1
       
        # 遍历计数器中的所有计数
        for count in hash_table.values():
           
            # 如果有任何字符的计数大于0，意味着杂志没有提供足够的该字符
            # 因此返回False
            if count > 0:
                return False
        
        # 如果所有字符的计数都是0或负数，意味着杂志提供了足够的字符
        # 因此返回True
        return True
