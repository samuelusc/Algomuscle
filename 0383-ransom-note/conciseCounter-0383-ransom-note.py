class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        # Subtracting Counters will only retain positive counts
        # and remove negative and zero counts
        return not Counter(ransomNote) - Counter(magazine)
        # 如果magzine 中每个字符数量大于等于ransomNote,则返回空        


        # return Counter(ransomNote) <= Counter(magazine)
        # 检查第一个计数器中的每个计数是否都不大于第二个计数器中相应字符的计数
