class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        majority = None

        for num in nums:
            if count == 0:
                majority = num
                count = 1

            elif majority == num:
                count += 1
            
            else:
                count -= 1
        
        return majority 