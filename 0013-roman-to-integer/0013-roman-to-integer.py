class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        left = 0
        
        while left < len(s):
            if left + 1 < len(s) and dic[s[left]] < dic[s[left + 1]]:
                total += dic[s[left + 1]] - dic[s[left]]
                left += 2
            else:
                total += dic[s[left]]
                left += 1
        
        return total

