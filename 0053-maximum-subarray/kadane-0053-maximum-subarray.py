class Solution:
    def maxSubArray(self, nums: List[int]) -> int:


        res, count = float('-inf'),float('-inf')
        for num in nums: 
            #现在的数值是取求和，或是重新以现在的数值开始
            count = num + max(count, 0)
            
            res = max(res, count)
        
        return res
